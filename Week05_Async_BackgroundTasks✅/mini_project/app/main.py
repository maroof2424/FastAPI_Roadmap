from fastapi import FastAPI
from .db import engine, Base
from .endpoints import router as mini_router

app = FastAPI(title="Mini Project – Async API with Background Tasks")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(mini_router)
