from fastapi import APIRouter,HTTPException
from app import schemas,crud
router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.get("/",response_model=list[schemas.PostOut])
def get_posts():
    return get_posts()

@router.get("/{post_id}",response_model=schemas.PostOut)
def get_post(post_id:int):
    post = crud.get_post_by_id(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.get("/",response_model=schemas.PostOut)
def create_post(post: schemas.PostCreate):
    return crud.create_post(post)