from typing import List, Optional
from sqlmodel import Session, select
from app.models.vendor import Vendor, VendorCreate

def create_vendor(session: Session, vendor: VendorCreate) -> Vendor:
    """Adds a new vendor to the database."""
    db_vendor = Vendor.model_validate(vendor)
    session.add(db_vendor)
    session.commit()
    session.refresh(db_vendor)
    return db_vendor

def get_all_vendors(session: Session) -> List[Vendor]:
    """Retrieves all vendors."""
    statement = select(Vendor)
    return session.exec(statement).all()

def get_vendor_by_id(session: Session, vendor_id: int) -> Optional[Vendor]:
    """Retrieves a single vendor by ID."""
    return session.get(Vendor, vendor_id)


