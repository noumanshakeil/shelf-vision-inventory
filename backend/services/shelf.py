from __future__ import annotations
import json
import re
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.models import RestockItem, ShelfScan, SkuDetection, StockGap
from backend.utils.ids import short_id
from backend.vision.confidence import aggregate_field_confidence
from backend.vision.pipeline import run_offline_pipeline

_SKU = re.compile(r"SKU[- ]?(\w+)", re.I)

async def ingest_scan(session: AsyncSession, aisle: str, raw_text: str, notes: str = "") -> ShelfScan:
    scan = ShelfScan(id=short_id(), aisle=aisle.strip()[:64], notes=notes.strip()[:2000])
    session.add(scan)
    await session.flush()
    pipe = run_offline_pipeline(raw_text, steps=["normalize", "ocr"])
    skus = _SKU.findall(pipe["text"]) or ["UNKNOWN"]
    confidences: list[float] = []
    for i, sku in enumerate(skus[:15]):
        conf = round(0.55 + (i % 4) * 0.1, 2)
        confidences.append(conf)
        session.add(
            SkuDetection(
                id=short_id(),
                scan_id=scan.id,
                sku=sku.upper()[:64],
                label=f"Facing {i+1}",
                confidence=conf,
                facings=1 + (i % 3),
            )
        )
    await session.commit()
    await session.refresh(scan)
    scan.notes = (scan.notes or "") + f" avg_conf={aggregate_field_confidence(confidences)}"
    await session.commit()
    return scan

async def compute_gaps(session: AsyncSession, scan_id: str, expected: dict[str, int]) -> list[StockGap]:
    dets = list(
        (await session.execute(select(SkuDetection).where(SkuDetection.scan_id == scan_id))).scalars()
    )
    observed = {d.sku: d.facings for d in dets}
    gaps: list[StockGap] = []
    for sku, exp in expected.items():
        obs = observed.get(sku, 0)
        if obs < exp:
            gap = StockGap(id=short_id(), scan_id=scan_id, sku=sku, expected=exp, observed=obs)
            session.add(gap)
            gaps.append(gap)
    await session.commit()
    return gaps

async def build_restock_list(session: AsyncSession, scan_id: str) -> list[RestockItem]:
    gaps = list((await session.execute(select(StockGap).where(StockGap.scan_id == scan_id))).scalars())
    items: list[RestockItem] = []
    for g in gaps:
        qty = max(g.expected - g.observed, 0)
        if qty <= 0:
            continue
        item = RestockItem(id=short_id(), sku=g.sku, qty=qty, reason="shelf_gap")
        session.add(item)
        items.append(item)
    await session.commit()
    return items

async def list_scans(session: AsyncSession) -> list[ShelfScan]:
    return list((await session.execute(select(ShelfScan).order_by(ShelfScan.created_at.desc()))).scalars())
