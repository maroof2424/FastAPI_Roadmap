from app import schemas

post_data = []

def get_posts():
    return post_data

def get_post_by_id(post_id: int):
    return next((post for post in post_data if post["id"] == post_id), None)

def create_post(post: schemas.PostCreate):
    new_id = len(post_data) + 1
    new_post = {"id": new_id, **post.dict()}
    post_data.append(new_post)
    return new_post

def update_post(post_id: int, post: schemas.PostCreate):
    existing_post = get_post_by_id(post_id)
    if existing_post:
        existing_post.update(post.dict())
        return existing_post
    return None

def delete_post(post_id: int):
    existing_post = get_post_by_id(post_id)
    if existing_post:
        post_data.remove(existing_post)
        return True
    return False

def search_posts(keyword: str):
    return [
        post for post in post_data
        if keyword.lower() in post["title"].lower() or keyword.lower() in post["content"].lower()
    ]
