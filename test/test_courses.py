import pytest
import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from core.configs import settings
from main import app
from models.course_model import CourseModel
from core.database import get_db as original_get_db

DATABASE_URL = settings.DB_URL

engine = create_async_engine(DATABASE_URL, echo=True)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

@pytest_asyncio.fixture(scope="module")
async def async_client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

@pytest_asyncio.fixture(scope="module")
async def db_session():
    async with engine.begin() as conn:
        await conn.run_sync(CourseModel.metadata.create_all)
    async with AsyncSession(engine) as session:
        yield session
    async with engine.begin() as conn:
        await conn.run_sync(CourseModel.metadata.drop_all)

@pytest_asyncio.fixture(scope="module")
def override_get_db(db_session):
    async def _override_get_db():
        yield db_session
    app.dependency_overrides[original_get_db] = _override_get_db

@pytest.mark.asyncio
async def test_create_course(async_client, override_get_db):
    payload = {
        "title": "Developer Jr",
        "classes": 5,
        "hours": 4
    }
    response = await async_client.post("/api/v1/courses/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["classes"] == payload["classes"]
    assert data["hours"] == payload["hours"]
