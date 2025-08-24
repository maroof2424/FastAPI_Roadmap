from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import get_db

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.post("/", response_model=schemas.PostOut)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    return crud.create_post(db, post)

@router.get("/", response_model=list[schemas.PostOut])
def read_posts(db: Session = Depends(get_db)):
    return crud.get_posts(db)

