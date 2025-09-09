from sqlalchemy import Column, Integer, String
from .db import Base

class ExternalData(Base):
    __tablename__ = "external_data"

    id = Column(Integer, primary_key=True, index=True)
    source = Column(String,nullable=False)
    content = Column(String, nullable=False)