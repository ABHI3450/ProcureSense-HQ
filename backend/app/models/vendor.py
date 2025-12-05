from typing import Optional
from sqlmodel import Field, SQLModel

class VendorBase(SQLModel):
    """Base class for Vendor properties."""
    name: str = Field(index=True)
    email: Optional[str] = None
    phone: Optional[str] = None
    rating: Optional[float] = Field(default=0.0)
    spend: Optional[float] = Field(default=0.0)

class Vendor(VendorBase, table=True):
    """Vendor table model."""
    id: Optional[int] = Field(default=None, primary_key=True)

class VendorCreate(VendorBase):
    """Model used for creating a new vendor."""
    pass

class VendorRead(VendorBase):
    """Model used for reading/returning vendor data."""
    id: int


