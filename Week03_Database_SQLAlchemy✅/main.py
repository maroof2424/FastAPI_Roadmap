from fastapi import FastAPI
from app import models
from app.database import engine
from app.routers import users,posts

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Blog API with Database")

app.include_router(users.router)
app.include_router(posts.router)
