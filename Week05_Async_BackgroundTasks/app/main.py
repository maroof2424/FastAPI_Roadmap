from fastapi import FastAPI
from .endpoints import router as async_router

app = FastAPI()

app.include_router(async_router)