from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from core.database import SessionLocal


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
