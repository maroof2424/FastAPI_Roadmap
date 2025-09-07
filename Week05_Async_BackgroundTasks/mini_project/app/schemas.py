from pydantic import BaseModel

class ExternalDataCreate(BaseModel):
    source: str
    content: str

class ExternalDataOut(BaseModel):
    id: int
    source: str
    content: str

    class Config:
        orm_mode = True