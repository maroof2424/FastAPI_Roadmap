from pydantic import BaseModel
from typing import Optional

class PostCreate(BaseModel):
    title: str
    content: str
    author: Optional[str] = "Anonymous"

class PostOut(BaseModel):
    id: int
    title: str
    content: str
    author: str

class Message(BaseModel):
    status: str
    message: str
