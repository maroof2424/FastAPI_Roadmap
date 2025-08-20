from fastapi import FastAPI
from app import models
from app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Blog API with Database")

@app.get("/")
def root():
    return {"message": "Blog API with SQLite + SQLAlchemy is ready!"}
