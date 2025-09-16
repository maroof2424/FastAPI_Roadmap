import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.db import Base, get_db
from app.main import app

# Test DB (SQLite in-memory)
TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"

engine_test = create_async_engine(TEST_DATABASE_URL, future=True, echo=False)
TestingSessionLocal = sessionmaker(bind=engine_test, class_=AsyncSession, expire_on_commit=False)

# Override DB
async def override_get_db():
    async with TestingSessionLocal() as session:
        yield session

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="function", autouse=True)
async def setup_db():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as c:
        yield c
