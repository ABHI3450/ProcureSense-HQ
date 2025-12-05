from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List
from app.models.contracts import ContractRead, ContractCreate, Contract
from app.services import contract_services as contract_service
from app.database.connection import get_session # Dependency for database access

router = APIRouter()

# --- CREATE (POST) ---
@router.post("/", response_model=ContractRead)
def create_new_contract(contract: ContractCreate, session: Session = Depends(get_session)):
    """Endpoint to create a new contract."""
    return contract_service.create_contract(session, contract)

# --- READ ALL (GET) ---
@router.get("/", response_model=List[ContractRead])
def read_all_contracts(session: Session = Depends(get_session)):
    """Endpoint to retrieve a list of all contracts."""
    return contract_service.get_all_contracts(session)

# --- READ ONE (GET) ---
@router.get("/{contract_id}", response_model=ContractRead)
def read_contract_by_id(contract_id: int, session: Session = Depends(get_session)):
    """Endpoint to retrieve a single contract by ID."""
    contract = contract_service.get_contract_by_id(session, contract_id)
    if not contract:
        raise HTTPException(status_code=404, detail="Contract not found")
    return contract