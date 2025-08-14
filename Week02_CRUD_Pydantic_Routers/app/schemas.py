from pydantic import BaseModel
from typing import Optional

class PostCreate(BaseModel):
    title : str
    content : str
    author : Optional[str] = "Anonymos"

class PostOut(BaseModel):
    id: int
    title: str
    content: str
    author:str