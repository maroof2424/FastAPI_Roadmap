import pytest

@pytest.mark.asyncio
async def test_create_user(client):
    response = await client.post("/users/", params={"username": "alice", "email": "alice@test.com"})
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "alice"
    assert data["email"] == "alice@test.com"
