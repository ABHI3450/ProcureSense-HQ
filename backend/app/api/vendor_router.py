from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List
from app.models.vendor import Vendor
from app.services import vendor_service as vendor_service
from app.database.connection import get_session

# --- THIS LINE MUST BE PRESENT AND CORRECTLY SPELLED ---
router = APIRouter() 

# --- CREATE (POST) ---
@router.post("/", response_model=Vendor)
def create_new_vendor(vendor: Vendor, session: Session = Depends(get_session)):
    """Endpoint to create a new vendor."""
    return vendor_service.create_vendor(session, vendor)

# --- READ ALL (GET) ---
@router.get("/", response_model=List[Vendor])
def read_all_vendors(session: Session = Depends(get_session)):
    """Endpoint to retrieve a list of all vendors."""
    return vendor_service.get_all_vendors(session)

# --- READ ONE (GET) ---
@router.get("/{vendor_id}", response_model=Vendor)
def read_vendor_by_id(vendor_id: int, session: Session = Depends(get_session)):
    """Endpoint to retrieve a single vendor by ID."""
    vendor = vendor_service.get_vendor_by_id(session, vendor_id)
    if not vendor:
        raise HTTPException(status_code=404, detail="Vendor not found")
    return vendor