from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    author: str
    title: str
    description: str

posts_db = {}

@app.get("/")
def read_posts():
    return posts_db

@app.post("/posts/")
def create_post(post: Post):
    post_id = len(posts_db) + 1
    posts_db[post_id] = post
    return {"id":post_id,"post":post}

@app.get("/posts/{post_id}")
def read_post(post_id:int):
    if post_id not in posts_db:
        raise HTTPException(status_code=404,detail="Post not found")
    return {"id":post_id,"post":posts_db[post_id]}

@app.put("/posts/{post_id}")
def update_post(post_id:int, update_post:Post):
    if post_id not in posts_db:
        raise HTTPException(status_code=404,detail="Post not found")
    posts_db[post_id] = update_post
    return {"id":post_id,"post":update_post}

@app.delete("/posts/{post_id}")
def delete_post(post_id:int, update_post:Post):
    if post_id not in posts_db:
        raise HTTPException(status_code=404,detail="Post not found")
    del posts_db[post_id]
    return {"message":f"Post {post_id} deleted successfully"}

