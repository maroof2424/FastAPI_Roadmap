from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from .db import get_db
from . import models, schemas, utils, tasks

router = APIRouter(prefix="/mini", tags=["Mini Project"])

@router.post("/fetch_store", response_model=schemas.ExternalDataOut)
async def fetch_and_store(
    background_tasks: BackgroundTasks,  
    db: AsyncSession = Depends(get_db)
):
    url = "https://api.github.com"
    data = await utils.fetch_data(url)

    new_record = models.ExternalData(
        source=url,
        content=str(data)
    )
    db.add(new_record)
    await db.commit()
    await db.refresh(new_record)

    background_tasks.add_task(
        tasks.send_email_notification,
        "test@example.com",
        f"New data stored with ID {new_record.id}"
    )

    return new_record


@router.get("/records", response_model=list[schemas.ExternalDataOut])
async def get_records(db: AsyncSession = Depends(get_db)):
    result = await db.execute(models.ExternalData.__table__.select())
    return result.fetchall()
