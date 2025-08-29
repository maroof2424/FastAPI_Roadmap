from fastapi import FastAPI
from app import models
from app.database import engine
from app.routers import users

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Auth with JWT")

app.include_router(users.router)
