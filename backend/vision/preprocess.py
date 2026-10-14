from __future__ import annotations
import re
from backend.utils.text import normalize

_NOISE = re.compile(r"[^\w\s.,:$/-]", re.UNICODE)

def normalize_scan_text(raw: str) -> str:
    clean = normalize(raw)
    return _NOISE.sub("", clean)

def simulate_deskew(meta: dict | None) -> dict:
    meta = dict(meta or {})
    meta.setdefault("deskew_deg", 0.0)
    meta["deskew_deg"] = float(meta.get("deskew_deg", 0.0))
    meta["simulated"] = True
    return meta
