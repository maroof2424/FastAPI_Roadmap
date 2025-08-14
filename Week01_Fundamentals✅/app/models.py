from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False

class ItemOut(BaseModel):
    name : str
    price: float
    