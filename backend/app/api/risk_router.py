from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List
from app.models.risk import RiskRead, RiskCreate
from app.services import risk_services as risk_service
from app.database.connection import get_session

router = APIRouter()

# --- CREATE (POST) ---
@router.post("/", response_model=RiskRead)
def create_new_risk_assessment(risk: RiskCreate, session: Session = Depends(get_session)):
    """Endpoint to create a new risk assessment."""
    return risk_service.create_risk_assessment(session, risk)

# --- READ BY CONTRACT (GET) ---
@router.get("/contract/{contract_id}", response_model=List[RiskRead])
def read_risks_by_contract(contract_id: int, session: Session = Depends(get_session)):
    """Endpoint to retrieve risk assessments by Contract ID."""
    risks = risk_service.get_risk_by_contract(session, contract_id)
    if not risks:
        raise HTTPException(status_code=404, detail="No risk assessments found for this contract.")
    return risks