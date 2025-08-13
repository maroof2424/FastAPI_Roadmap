from fastapi import APIRouter

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

post_data = [
    {"id":1,"title":"First Post","content":"This is my first blog post"},
    {"id":2,"title":"Second Post","content":"Learning FastAPI is fun!"},
]

@router.get("/")
def get_posts():
    return {"status":"success","data":post_data}

    