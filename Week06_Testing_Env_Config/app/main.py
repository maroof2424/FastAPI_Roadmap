from fastapi import FastAPI, Depends
from .config import settings
from .dependencies import get_current_user

app = FastAPI(title=settings.app_name)

# Healthcheck
@app.get("/")
def healthcheck():
    return {"status": "ok"}

# Show loaded configs
@app.get("/config")
def get_config():
    return {
        "app_name": settings.app_name,
        "debug": settings.debug,
        "database_url": settings.database_url,
    }

# Protected route
@app.get("/protected")
async def protected_route(current_user: dict = Depends(get_current_user)):
    return {"message": f"Hello {current_user['username']}"}
