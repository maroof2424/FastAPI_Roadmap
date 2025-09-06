from fastapi import FastAPI
from .endpoints import router as async_router
from .db import engine, Base
from . import demo,models,tasks,external


app = FastAPI(title="Async FastAPI + SQLite")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(demo.router)
app.include_router(async_router)
app.include_router(tasks.router) 
app.include_router(external.router) 