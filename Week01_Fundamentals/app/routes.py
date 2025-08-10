from fastapi import APIRouter
from app.models import Item,ItemOut

router = APIRouter()

# @router.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "query": q}

@router.post("/items/")
def create_item(item: Item):
    return item
@router.get("/items/{item_id}/",response_model=ItemOut, tags=["Items"], summary="Get a specific item", description="Retrieve an item by its ID from the product catalog.")
def read_item(item_id:int):
    return{"name":"Laptop","price":"99.9","is_offer":True}  