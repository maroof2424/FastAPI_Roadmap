from fastapi import FastAPI
from app.routers import posts

app = FastAPI(title="Blog API - Week 2 CRUD")

app.include_router(posts.router)

@app.get("/")
def root():
    return {"message":"Welcome to Blog API."}