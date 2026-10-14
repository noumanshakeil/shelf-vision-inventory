from __future__ import annotations
from backend.vision.metadata import parse_stub_metadata
from backend.vision.preprocess import normalize_scan_text, simulate_deskew
from backend.vision.stubs import mock_ocr_lines

def run_offline_pipeline(text: str, *, meta: dict | None = None, steps: list[str] | None = None) -> dict:
    steps = steps or ["normalize", "deskew", "ocr"]
    meta_out = parse_stub_metadata(meta)
    body = text
    lines: list[dict] = []
    for step in steps:
        if step == "normalize":
            body = normalize_scan_text(body)
        elif step == "deskew":
            meta_out = simulate_deskew(meta_out)
        elif step == "ocr":
            lines = mock_ocr_lines(body)
    return {"text": body, "metadata": meta_out, "lines": lines, "steps": steps}
