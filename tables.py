import asyncio
from core.configs import settings
from core.database import engine
from models.course_model import CourseModel  # Certifique-se de importar o modelo

async def create_tables():
    # Verificação adicional para garantir que os metadados incluem a tabela
    print("Loaded tables before create_all:", settings.DBBaseModel.metadata.tables)
    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
        print('Tables created')
        # Verificação adicional após a criação das tabelas
        print("Loaded tables after create_all:", settings.DBBaseModel.metadata.tables)
        return True

if __name__ == '__main__':
    asyncio.run(create_tables())
