from __future__ import annotations
from backend.vision.validators import clamp_confidence

def aggregate_field_confidence(scores: list[float]) -> float:
    if not scores:
        return 0.0
    vals = [clamp_confidence(s) for s in scores]
    return round(sum(vals) / len(vals), 3)
