from app import schemas

post_data = [
    {"id": 1, "title": "First Post", "content": "This is my first blog post", "author": "Maroof"},
    {"id": 2, "title": "Second Post", "content": "Learning FastAPI is fun!", "author": "Maroof"},
]

def get_post():
    return post_data

def create_post(post:schemas.PostCreate):
    new_id = len(post_data)+1
    new_post = {'id':new_id,**post.dict()}
    post_data.append(new_post)
    return new_post

def get_post_by_id(post_id:int):
    for post in post_data:
        if post["id"] == post_id:
            return post
    return None
    

def update_post(post_id: int, post: schemas.PostCreate):
    existing_Post = get_post_by_id(post_id)
    if existing_Post:
        existing_Post.update(post.dict())
        return existing_Post
    return None

def delete_post(post_id: int):
    existing_post = get_post_by_id(post_id)
    if existing_post:
        post_data.remove(existing_post)
        return True
    return False

def search_posts(keyword:str):
    results = []
    for post in post_data:
        if keyword.lower() in post["title"].lower() or keyword.lower() in post["content"].lower():
            results.append(post)
    return results