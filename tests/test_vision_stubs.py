from backend.vision.stubs import mock_ocr_lines

def test_mock_ocr_splits_sentences():
    lines = mock_ocr_lines("A. B. C.")
    assert len(lines) >= 2
