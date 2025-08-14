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
    