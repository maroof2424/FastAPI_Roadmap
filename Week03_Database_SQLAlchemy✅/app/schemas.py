from pydantic import BaseModel
from typing import List,Optional

class UserCreate(BaseModel):
    username: str
    email: str

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    posts: List["PostOut"] = []
    class Config:
        from_attributes = True



class PostCreate(BaseModel):
    title: str
    content: str
    author_id: int

class PostOut(BaseModel):
    id: int
    title: str
    content: str
    author_id: int

    class Config:
        from_attributes = True
