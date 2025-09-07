from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .db import get_db
from . import models,schemas,utils

router = APIRouter(prefix="/mini",tags=["Mini Project"])

@router.post("/fetch_store",response_model=schemas.ExternalDataOut)
async def fetch_and_store(db: AsyncSession = Depends(get_db)):
    url = "https://api.github.com"
    data = await utils.fetch_data(url)

    new_record = models.ExternalData(
        source=url,
        content=str(data)
    )
    db.add(new_record)
    await db.commit()
    await db.refresh(new_record)

    return new_record

@router.get("/records", response_model=list[schemas.ExternalDataOut])
async def get_records(db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        models.ExternalData.__table__.select()
    )
    return result.fetchall()