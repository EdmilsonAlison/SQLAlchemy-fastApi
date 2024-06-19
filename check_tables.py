import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy import text

DATABASE_URL = "postgresql+asyncpg://postgres:rootxvk9@localhost:5432/fastapi"

engine: AsyncEngine = create_async_engine(DATABASE_URL, echo=True)

async def check_tables():
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"))
        tables = result.fetchall()
        print("Tables in database:", tables)
        await conn.commit()

if __name__ == '__main__':
    asyncio.run(check_tables())
