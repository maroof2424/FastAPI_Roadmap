from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db import get_db
from app import models

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.post("/")
async def create_post(title: str, content: str, owner_id: int, db: AsyncSession = Depends(get_db)):
    post = models.Post(title=title, content=content, owner_id=owner_id)
    db.add(post)
    await db.commit()
    await db.refresh(post)
    return post

@router.get("/")
async def list_posts(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Post))
    return result.scalars().all()
