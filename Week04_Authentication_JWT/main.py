from fastapi import FastAPI
from app import models
from app.database import engine
from app.routers import users, posts, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI JWT Auth Example")

app.include_router(users.router)
app.include_router(posts.router)
app.include_router(auth.router)
