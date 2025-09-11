from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./app.db")

engine = create_async_engine(DATABASE_URL, echo=True, future=True)

async_sessionmaker = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

Base = declarative_base()

async def get_db() -> AsyncSession:
    async with async_sessionmaker() as session:
        yield session
