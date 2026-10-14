# Dev server for shelf-vision-inventory
$env:LLM_MODE = "mock"
uvicorn backend.main:app --reload --port 8000
