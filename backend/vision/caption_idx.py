from __future__ import annotations
from backend.utils.text import token_set

def caption_overlap(query: str, caption: str) -> float:
    q, c = token_set(query), token_set(caption)
    if not q or not c:
        return 0.0
    return len(q & c) / len(q | c)
