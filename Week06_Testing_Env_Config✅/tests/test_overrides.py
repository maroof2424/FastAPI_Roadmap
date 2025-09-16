import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.dependencies import get_db, get_current_user

async def override_get_db():
    yield None  

async def override_get_current_user():
    return {"id": 1, "username": "testuser"}

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

client = TestClient(app)

def test_protected_route():
    response = client.get("/protected")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello testuser"}
