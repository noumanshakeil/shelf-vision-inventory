from __future__ import annotations
from datetime import datetime
from sqlalchemy import DateTime, Float, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from backend.db import Base

def utcnow(): return datetime.utcnow()

class ShelfScan(Base):
    __tablename__ = "shelf_scans"
    id: Mapped[str] = mapped_column(String(32), primary_key=True)
    aisle: Mapped[str] = mapped_column(String(64), index=True)
    notes: Mapped[str] = mapped_column(Text, default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=utcnow)

class SkuDetection(Base):
    __tablename__ = "sku_detections"
    id: Mapped[str] = mapped_column(String(32), primary_key=True)
    scan_id: Mapped[str] = mapped_column(String(32), index=True)
    sku: Mapped[str] = mapped_column(String(64), index=True)
    label: Mapped[str] = mapped_column(String(160), default="")
    confidence: Mapped[float] = mapped_column(Float, default=0.0)
    facings: Mapped[int] = mapped_column(Integer, default=1)

class StockGap(Base):
    __tablename__ = "stock_gaps"
    id: Mapped[str] = mapped_column(String(32), primary_key=True)
    scan_id: Mapped[str] = mapped_column(String(32), index=True)
    sku: Mapped[str] = mapped_column(String(64), index=True)
    expected: Mapped[int] = mapped_column(Integer, default=0)
    observed: Mapped[int] = mapped_column(Integer, default=0)

class RestockItem(Base):
    __tablename__ = "restock_items"
    id: Mapped[str] = mapped_column(String(32), primary_key=True)
    sku: Mapped[str] = mapped_column(String(64), index=True)
    qty: Mapped[int] = mapped_column(Integer, default=0)
    reason: Mapped[str] = mapped_column(String(120), default="gap")
