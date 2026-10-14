#!/usr/bin/env python3
# Seed demo rows via HTTP (server must be running).
from __future__ import annotations
import httpx

BASE = "http://127.0.0.1:8000"

def main() -> None:
    r = httpx.get(BASE + "/health", timeout=10)
    print("health", r.status_code, r.text[:120])

if __name__ == "__main__":
    main()
