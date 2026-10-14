"""Simulated vision pipeline (text/metadata stubs — no GPU required)."""
from backend.vision.preprocess import normalize_scan_text, simulate_deskew
from backend.vision.stubs import mock_ocr_lines
from backend.vision.pipeline import run_offline_pipeline

__all__ = [
    "normalize_scan_text",
    "simulate_deskew",
    "mock_ocr_lines",
    "run_offline_pipeline",
]
