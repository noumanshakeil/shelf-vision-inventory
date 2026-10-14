from fastapi import APIRouter
from backend.api import health, shelf, ui
api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(shelf.router, prefix="/api", tags=["shelf"])
api_router.include_router(ui.router, tags=["ui"])
