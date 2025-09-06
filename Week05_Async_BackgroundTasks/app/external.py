from fastapi import APIRouter
from .utils import fetch_data

router = APIRouter(prefix="/external", tags=["External API"])

@router.get("/")
async def get_external_data():
    url = "https://api.github.com"
    data = await fetch_data(url)
    return {"source": url, "data": data}