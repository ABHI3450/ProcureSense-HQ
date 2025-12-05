from typing import List, Optional
from sqlmodel import Session, select
from app.models.contracts import Contract, ContractCreate

def create_contract(session: Session, contract: ContractCreate) -> Contract:
    """Adds a new contract to the database."""
    db_contract = Contract.model_validate(contract)
    session.add(db_contract)
    session.commit()
    session.refresh(db_contract)
    return db_contract

def get_all_contracts(session: Session) -> List[Contract]:
    """Retrieves all contracts."""
    statement = select(Contract)
    return session.exec(statement).all()

def get_contract_by_id(session: Session, contract_id: int) -> Optional[Contract]:
    """Retrieves a single contract by ID."""
    return session.get(Contract, contract_id)