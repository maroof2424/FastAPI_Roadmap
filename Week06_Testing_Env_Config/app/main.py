from fastapi import FastAPI, Depends
from app.config import settings
from app.dependencies import get_current_user
from app.db import Base, engine
from app.routers import users, posts

app = FastAPI(title=settings.app_name)

@app.get("/")
def healthcheck():
    return {"status": "ok"}

@app.get("/config")
def get_config():
    return {
        "app_name": settings.app_name,
        "debug": settings.debug,
        "database_url": settings.database_url,
    }

@app.get("/protected")
async def protected_route(current_user: dict = Depends(get_current_user)):
    return {"message": f"Hello {current_user['username']}"}

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(users.router)
app.include_router(posts.router)
