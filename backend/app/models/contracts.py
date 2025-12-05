from __future__ import annotations
from typing import Optional
from datetime import date
from sqlmodel import Field, SQLModel

class ContractBase(SQLModel):
    """Base class for Contract properties."""
    title: str = Field(index=True)
    vendor_id: int = Field(index=True)
    start_date: date
    end_date: date
    total_value: float
    summary_ai: Optional[str] = None
    status: str = Field(default="Active", index=True)

class Contract(ContractBase, table=True):
    """Contract table model."""
    id: Optional[int] = Field(default=None, primary_key=True)

class ContractCreate(ContractBase):
    """Model used when creating a new contract (ID is excluded)."""
    pass

class ContractRead(ContractBase):
    """Model used for reading/returning contract data."""
    id: int
