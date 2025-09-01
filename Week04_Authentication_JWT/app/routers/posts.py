from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, models
from app.dependencies import get_db, get_current_user

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.post("/", response_model=schemas.PostOut)
def create_post(
    post: schemas.PostCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    new_post = models.Post(
        title=post.title,
        content=post.content,
        author_id=current_user.id   
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/", response_model=list[schemas.PostOut])
def get_posts(db: Session = Depends(get_db)):
    return db.query(models.Post).all()
