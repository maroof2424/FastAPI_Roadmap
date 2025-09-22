# app/main.py
from fastapi import FastAPI, Depends
from app.config import settings

app = FastAPI(title=settings.app_name)

@app.get("/")
def healthcheck():
    return {"status": "ok", "debug": settings.debug}

@app.get("/config")
def get_config():
    return {
        "app_name": settings.app_name,
        "debug": settings.debug,
        "secret_key": settings.secret_key,
        "database_url": settings.database_url,
    }
