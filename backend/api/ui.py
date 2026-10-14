from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from backend.db import get_db
from backend.services import shelf as svc

router = APIRouter()
templates = Jinja2Templates(directory="backend/templates")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request, db: AsyncSession = Depends(get_db)):
    scans = await svc.list_scans(db)
    return templates.TemplateResponse("index.html", {"request": request, "title": "Shelf Vision Inventory", "scans": scans})

@router.post("/ui/scans")
async def ui_scan(aisle: str = Form(...), raw_text: str = Form(...), db: AsyncSession = Depends(get_db)):
    scan = await svc.ingest_scan(db, aisle, raw_text)
    await svc.compute_gaps(db, scan.id, {"SKU-100": 4, "SKU-200": 2})
    await svc.build_restock_list(db, scan.id)
    return RedirectResponse("/", status_code=303)
