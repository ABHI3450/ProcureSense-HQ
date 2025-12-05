from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = "sqlite:///./procuresense.db"

    # AI Service - CHANGED to GROQ_API_KEY
    GROQ_API_KEY: Optional[str] = None
    LLM_MODEL: str = "llama3-8b-8192" 

    # Application
    SECRET_KEY: str = "dev-secret-key-change-in-production"
    ENVIRONMENT: str = "development"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()