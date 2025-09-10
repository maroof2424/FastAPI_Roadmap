from fastapi import FastAPI
from .config import settings

app = FastAPI(title=settings.app_name)

@app.get("/")
def healthcheck():
    return {"status": "ok"}

@app.get("/config")
def get_config():
    return {
        "app_name":settings.app_name,
        "debug":settings.debug,
        "database_url":settings.database_url,
    }