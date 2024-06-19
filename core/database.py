from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from core.configs import settings

engine: AsyncEngine = create_async_engine(settings.DB_URL, echo=True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
)

async def get_db():
    async with SessionLocal() as session:
        yield session
