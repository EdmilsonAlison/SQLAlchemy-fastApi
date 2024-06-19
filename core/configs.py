from typing import ClassVar
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    """
    Settings class for the FastAPI app
    """
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://postgres:rootxvk9@localhost:5432/fastapi"
    DBBaseModel: ClassVar = declarative_base()

    class Config:
        case_sensitive = True

settings = Settings()
