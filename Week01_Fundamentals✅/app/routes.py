# from fastapi import APIRouter,HTTPException
# from app.models import Item,ItemOut

# router = APIRouter()

# # # @router.get("/items/{item_id}")
# # # def read_item(item_id: int, q: str = None):
# # #     return {"item_id": item_id, "query": q}

# # @router.post("/items/")
# # def create_item(item: Item):
# #     return item
# # @router.get("/items/{item_id}/",response_model=ItemOut, tags=["Items"], summary="Get a specific item", description="Retrieve an item by its ID from the product catalog.")
# # def read_item(item_id:int):
# #     return{"name":"Laptop","price":"99.9","is_offer":True}  

# products_db = {
#     1:{"name":"Mouse","price":25.0,"is_offer":True},
#     2:{"name":"Keyboard","price":50.0,"is_offer":False},
# }

# from fastapi import APIRouter, HTTPException
# from .models import Item, ItemOut

# router = APIRouter()

# # Dummy database
# products_db = {
#     1: {"name": "Mouse", "price": 25.0, "is_offer": True},
#     2: {"name": "Keyboard", "price": 50.0, "is_offer": False}
# }

# @router.get("/products", response_model=list[ItemOut])
# def get_products():
#     return list(products_db.values())

# @router.get("/products/{id}", response_model=ItemOut)
# def get_product(id: int):
#     if id not in products_db:
#         raise HTTPException(status_code=404, detail="Product not found")
#     return products_db[id]

# @router.post("/products", response_model=ItemOut)
# def create_product(item: Item):
#     new_id = max(products_db.keys()) + 1
#     products_db[new_id] = item.dict()
#     return item

# @router.put("/products/{id}", response_model=ItemOut)
# def update_product(id: int, item: Item):
#     if id not in products_db:
#         raise HTTPException(status_code=404, detail="Product not found")
#     products_db[id] = item.dict()
#     return item

# @router.delete("/products/{id}")
# def delete_product(id: int):
#     if id not in products_db:
#         raise HTTPException(status_code=404, detail="Product not found")
#     del products_db[id]
#     return {"detail": "Product deleted successfully"}

#     return {"detail":"Product delete successfully"}
from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Item  # Import your Pydantic model

router = APIRouter()

items = {}

@router.post("/items/", response_model=Item)
def create_item(item: Item):
    if item.id in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item.id] = item
    return item

@router.get("/items/", response_model=List[Item])
def read_items():
    return list(items.values())

@router.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    if item_id != updated_item.id:
        raise HTTPException(status_code=400, detail="Item ID cannot be changed")
    items[item_id] = updated_item
    return updated_item

@router.delete("/items/{item_id}", response_model=dict)
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"detail": "Item deleted"}
