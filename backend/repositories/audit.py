from __future__ import annotations
from datetime import datetime, timezone

_EVENTS: list[dict] = []

def record(event: str, detail: str = "") -> None:
    _EVENTS.append(
        {"event": event, "detail": detail[:500], "at": datetime.now(timezone.utc).isoformat()}
    )

def recent(limit: int = 20) -> list[dict]:
    return list(reversed(_EVENTS[-limit:]))
