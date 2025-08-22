from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app import models,schemas
from app.database import get_db

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.get("/",response_model=list[schemas.PostOut])
def get_posts(db: Session = Depends(get_db)):
    return db.query(models.Post).all()

@router.post("/",response_model=schemas.PostOut)
def create_post(post:schemas.PostCreate,db:Session=Depends(get_db)):
    new_post = models.Post(title=post.title,content=post.content,author_id = post.author_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post