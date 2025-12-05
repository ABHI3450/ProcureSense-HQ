from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.ai_router import router as ai_router
from app.api.vendor_router import router as vendor_router
from app.api.contract_router import router as contract_router
from app.api.risk_router import router as risk_router
from app.database.connection import create_db_and_tables

app = FastAPI(title="ProcureAI Command Center")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(ai_router, prefix="/ai", tags=["ai"])
app.include_router(vendor_router, prefix="/vendors", tags=["vendors"])
app.include_router(contract_router, prefix="/contracts", tags=["contracts"])
app.include_router(risk_router, prefix="/risks", tags=["risks"])

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def home():
    return {"message": "ProcureAI Backend Running"}
