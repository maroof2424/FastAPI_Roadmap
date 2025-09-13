import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.dependencies import get_current_user

client = TestClient(app)

@pytest.fixture
def test_user(db_session):
    from app import models, utils
    user = models.User(
        username="testuser",
        email="test@example.com",
        password=utils.hash_password("testpass")
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user

def test_login_token(test_user):
    response = client.post(
        "/auth/token",
        data={"username": "test@example.com", "password": "testpass"},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_protected_route_with_jwt(test_user):
    login = client.post(
        "/auth/token",
        data={"username": "test@example.com", "password": "testpass"},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    token = login.json()["access_token"]

    response = client.get(
        "/users/me",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"

def test_protected_route_without_token():
    response = client.get("/users/me")
    assert response.status_code == 401
    assert response.json()["detail"] == "Not authenticated"
