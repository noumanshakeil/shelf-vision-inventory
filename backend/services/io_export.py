from __future__ import annotations
import json
from backend.vision.export_io import rows_to_csv

def dump_json(payload: dict | list) -> str:
    return json.dumps(payload, indent=2, default=str)

def dump_csv(fieldnames: list[str], rows: list[dict]) -> str:
    return rows_to_csv(fieldnames, rows)
