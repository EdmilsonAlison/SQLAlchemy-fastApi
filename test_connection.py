import asyncio

import asyncpg


async def test_connection():
    conn = await asyncpg.connect("postgresql+asyncpg://postgres:rootxvk9@localhost:5432/fastapi")
    print("Connection successful")
    await conn.close()


if __name__ == "__main__":
    asyncio.run(test_connection())
