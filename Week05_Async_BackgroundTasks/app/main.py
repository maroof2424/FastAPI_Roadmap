from fastapi import FastAPI
from .endpoints import router as async_router
from . import engine, Base
from . import demo, models

app = FastAPI(title="Async FastAPI + SQLite")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# ✅ Add root route
@app.get("/")
async def root():
    return {"message": "Welcome to Async FastAPI + SQLite 🚀"}

app.include_router(demo.router)
app.include_router(async_router)
