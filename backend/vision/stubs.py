from __future__ import annotations
from backend.vision.preprocess import normalize_scan_text

def mock_ocr_lines(text: str) -> list[dict]:
    clean = normalize_scan_text(text)
    if not clean:
        return []
    lines = [ln.strip() for ln in clean.split(".") if ln.strip()]
    out: list[dict] = []
    for i, ln in enumerate(lines[:12]):
        out.append({"line": i + 1, "text": ln, "confidence": round(0.62 + (i % 5) * 0.07, 2)})
    return out
