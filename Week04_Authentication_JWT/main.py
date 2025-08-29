from fastapi import FastAPI
from app import models
from app.database import engine
from app.routers import users
from app import auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="JWT Auth API")

app.include_router(users.router)
app.include_router(auth.router)
