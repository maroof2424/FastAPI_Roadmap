from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite+aiosqlite:///./mini_project.db"

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLoacl = sessionmaker(bind=engine,class_=AsyncSession,expire_on_commit=False)
Base = declarative_base()

async def get_db():
    async with SessionLoacl() as session:
        yield session
        