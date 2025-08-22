from fastapi import FastAPI
from app import models
from app.database import engine
from app.routers import users

# Create DB tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Blog API with Database")

# ✅ Use router object
app.include_router(users.router)
