# Shelf Vision Inventory

Shelf image inventory counter with SKU hints and stock discrepancy UI.

## Stack

- **Backend:** FastAPI + Jinja UI (full-stack single service)
- **LLM:** mock provider by default; optional OpenAI / Ollama via env
- **Packaging:** Docker + docker-compose
- **Tests:** pytest API smoke tests

## Architecture

```text
Browser UI ──► FastAPI routes ──► domain store (JSON)
                   │
                   └──► llm.complete() (mock | openai | ollama)
```

## Quick start (local)

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn backend.main:app --reload --port 8000
```

Open http://127.0.0.1:8000

## Docker

```bash
docker compose up --build
```

## API

- `GET /health`
- `GET /api/shelves`
- `POST /api/shelves`
- `POST /api/count_stock` — Estimate shelf stock and gaps

## Tests

```bash
pytest -q
```

## Notes

Production-shaped learning app: real routes, UI, Docker, and tests. Swap `LLM_MODE=openai` or `ollama` when you have credentials/models.
