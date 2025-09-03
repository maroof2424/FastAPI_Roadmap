from fastapi import APIRouter
import asyncio

router = APIRouter()

@router.get("/sync")
def sync_endpoint():
    import time
    time.sleep(3)
    return {"message":"This was slow (sync)"}

@router.get("/async")
async def async_endpoint():
    await asyncio.sleep(3)
    return {"message":"This is fast (async,non-blocking)"}