import os
from typing import ClassVar

from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()


class Settings(BaseSettings):
    """
    Settings class for the FastAPI app
    """
    API_V1_STR: str = "/api/v1"
    DB_URL: str = os.getenv("DB_URL")
    DBBaseModel: ClassVar = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()
