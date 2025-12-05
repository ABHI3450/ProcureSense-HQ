from typing import Generator
from sqlmodel import create_engine, Session, SQLModel
from app.config import settings

# Engine setup using the DATABASE_URL from your .env (PostgreSQL)
# echo=True is helpful for seeing SQL statements run in the terminal
engine = create_engine(settings.DATABASE_URL, echo=True) 

def create_db_and_tables():
    """Initializes the database engine and creates tables defined in models."""
    # Ensure all models are imported here before calling create_all
    from app.models import vendor, contracts, risk
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[Session, None, None]:
    """Dependency function to provide a database session to FastAPI routes."""
    with Session(engine) as session:
        yield session