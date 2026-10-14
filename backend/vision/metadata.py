from __future__ import annotations

def parse_stub_metadata(raw: dict | None) -> dict:
    raw = raw or {}
    return {
        "width": int(raw.get("width", 1280)),
        "height": int(raw.get("height", 720)),
        "mime": str(raw.get("mime", "image/jpeg")),
        "source": str(raw.get("source", "upload")),
        "pages": int(raw.get("pages", 1)),
    }
