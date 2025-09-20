from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import Column, Integer, String, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from typing import List
from .config import settings

# ---------- Database ----------
DATABASE_URL = settings.database_url

engine = create_async_engine(DATABASE_URL, echo=True, future=True)
async_session_maker = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()


async def get_db():
    async with async_session_maker() as session:
        yield session


# ---------- Models ----------
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)


# ---------- Schemas ----------
class ItemCreate(BaseModel):
    name: str
    description: str | None = None


class ItemOut(BaseModel):
    id: int
    name: str
    description: str | None

    class Config:
        from_attributes = True   # ✅ Pydantic v2 fix


# ---------- App ----------
app = FastAPI(title="FastAPI CRUD with SQLite")


@app.on_event("startup")
async def startup():
    """Create tables on startup"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# ---------- CRUD Routes ----------
@app.post("/items/", response_model=ItemOut)
async def create_item(item: ItemCreate, db: AsyncSession = Depends(get_db)):
    new_item = Item(name=item.name, description=item.description)
    db.add(new_item)
    await db.commit()
    await db.refresh(new_item)
    return new_item


@app.get("/items/", response_model=List[ItemOut])
async def get_items(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Item))
    return result.scalars().all()


@app.get("/items/{item_id}", response_model=ItemOut)
async def get_item(item_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.get(Item, item_id)
    if not result:
        raise HTTPException(status_code=404, detail="Item not found")
    return result


@app.put("/items/{item_id}", response_model=ItemOut)
async def update_item(item_id: int, item: ItemCreate, db: AsyncSession = Depends(get_db)):
    db_item = await db.get(Item, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")

    db_item.name = item.name
    db_item.description = item.description
    await db.commit()
    await db.refresh(db_item)
    return db_item


@app.delete("/items/{item_id}")
async def delete_item(item_id: int, db: AsyncSession = Depends(get_db)):
    db_item = await db.get(Item, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")

    await db.delete(db_item)
    await db.commit()
    return {"message": "Item deleted successfully"}
