import pytest

@pytest.mark.asyncio
async def test_create_post(client):
    # First create a user
    user = await client.post("/users/", params={"username": "bob", "email": "bob@test.com"})
    user_id = user.json()["id"]

    # Create post
    response = await client.post("/posts/", params={"title": "Test Post", "content": "Hello!", "owner_id": user_id})
    assert response.status_code == 200
    post_data = response.json()
    assert post_data["title"] == "Test Post"
    assert post_data["owner_id"] == user_id

@pytest.mark.asyncio
async def test_list_posts(client):
    response = await client.get("/posts/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
