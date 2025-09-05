from fastapi import FastAPI
from .endpoints import router as async_router
from .db import engine, Base
from . import demo
from . import tasks  # 👈 import tasks router
from . import models

app = FastAPI(title="Async FastAPI + SQLite")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(demo.router)
app.include_router(async_router)
app.include_router(tasks.router)  # 👈 include tasks router
