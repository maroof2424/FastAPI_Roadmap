from pydantic import BaseModel, EmailStr
from typing import List, Optional

class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(PostBase):
    pass


class PostOut(PostBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserOut(UserBase):
    id: int
    posts: List[PostOut] = []

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
