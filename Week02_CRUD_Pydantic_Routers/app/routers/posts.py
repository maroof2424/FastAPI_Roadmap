from fastapi import APIRouter
from app import schemas,crud
router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.get("/",response_model=list[schemas.PostOut])
def get_posts():
    return get_posts()

@router.get("/",response_model=schemas.PostOut)
def create_post(post: schemas.PostCreate):
    return crud.create_post(post)