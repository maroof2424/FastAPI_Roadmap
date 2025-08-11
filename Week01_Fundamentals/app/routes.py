from fastapi import APIRouter,HTTPException
from app.models import Item,ItemOut

router = APIRouter()

# # @router.get("/items/{item_id}")
# # def read_item(item_id: int, q: str = None):
# #     return {"item_id": item_id, "query": q}

# @router.post("/items/")
# def create_item(item: Item):
#     return item
# @router.get("/items/{item_id}/",response_model=ItemOut, tags=["Items"], summary="Get a specific item", description="Retrieve an item by its ID from the product catalog.")
# def read_item(item_id:int):
#     return{"name":"Laptop","price":"99.9","is_offer":True}  

products_db = {
    1:{"name":"Mouse","price":25.0,"is_offer":True},
    2:{"name":"Keyboard","price":50.0,"is_offer":False},
}

from fastapi import APIRouter, HTTPException
from .models import Item, ItemOut

router = APIRouter()

# Dummy database
products_db = {
    1: {"name": "Mouse", "price": 25.0, "is_offer": True},
    2: {"name": "Keyboard", "price": 50.0, "is_offer": False}
}

@router.get("/products", response_model=list[ItemOut])
def get_products():
    return list(products_db.values())

@router.get("/products/{id}", response_model=ItemOut)
def get_product(id: int):
    if id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    return products_db[id]

@router.post("/products", response_model=ItemOut)
def create_product(item: Item):
    new_id = max(products_db.keys()) + 1
    products_db[new_id] = item.dict()
    return item

@router.put("/products/{id}", response_model=ItemOut)
def update_product(id: int, item: Item):
    if id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    products_db[id] = item.dict()
    return item

@router.delete("/products/{id}")
def delete_product(id: int):
    if id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    del products_db[id]
    return {"detail": "Product deleted successfully"}

    return {"detail":"Product delete successfully"}