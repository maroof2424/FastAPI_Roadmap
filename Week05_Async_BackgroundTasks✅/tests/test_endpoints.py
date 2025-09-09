import pytest
from httpx import AsyncClient
from app.main import app
from app.db import AsyncSessionLocal,Base,engine
import asyncio

@pytest.fixture(scope="module",autouse=True)
async def setup_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.mark.anyio
async def test_fetch_and_store():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/mini/fetch_store")
    assert response.status_code == 200
    json_data = response.json()
    assert "id" in json_data
    assert json_data["source"] == "https://api.github.com"

@pytest.mark.anyio
async def test_get_records():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/mini/records")
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data, list)
    if json_data:
        assert "id" in json_data[0]
        assert "source" in json_data[0]