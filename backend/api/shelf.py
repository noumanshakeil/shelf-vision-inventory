from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession
from backend.db import get_db
from backend.services import shelf as svc

class ScanIn(BaseModel):
    aisle: str = Field(min_length=1)
    raw_text: str = Field(min_length=3)
    notes: str = ""

class GapIn(BaseModel):
    expected: dict[str, int] = Field(default_factory=dict)

router = APIRouter()

@router.post("/scans")
async def create_scan(payload: ScanIn, db: AsyncSession = Depends(get_db)):
    scan = await svc.ingest_scan(db, payload.aisle, payload.raw_text, payload.notes)
    return {"id": scan.id, "aisle": scan.aisle}

@router.get("/scans")
async def scans(db: AsyncSession = Depends(get_db)):
    rows = await svc.list_scans(db)
    return {"scans": [{"id": s.id, "aisle": s.aisle} for s in rows]}

@router.post("/scans/{scan_id}/gaps")
async def gaps(scan_id: str, payload: GapIn, db: AsyncSession = Depends(get_db)):
    rows = await svc.compute_gaps(db, scan_id, payload.expected)
    return {"gaps": [{"sku": g.sku, "expected": g.expected, "observed": g.observed} for g in rows]}

@router.post("/scans/{scan_id}/restock")
async def restock(scan_id: str, db: AsyncSession = Depends(get_db)):
    items = await svc.build_restock_list(db, scan_id)
    return {"items": [{"sku": i.sku, "qty": i.qty} for i in items]}
