from backend.vision.pipeline import run_offline_pipeline

def test_offline_pipeline_returns_lines():
    out = run_offline_pipeline("Invoice 100. Total $42.", steps=["normalize", "ocr"])
    assert out["text"]
    assert out["lines"]
