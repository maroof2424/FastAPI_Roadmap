from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from .db import async_sessionmaker  
from . import models

async def get_db() -> AsyncSession:
    async with async_sessionmaker() as session:
        yield session

async def get_current_user():
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Not authenticated"
    )
