from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from app import models

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
async def create_user(username: str, email: str, db: AsyncSession = Depends(get_db)):
    user = models.User(username=username, email=email)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
