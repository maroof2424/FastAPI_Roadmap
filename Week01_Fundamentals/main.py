from fastapi import FastAPI
from app.routes import router as item_router

app = FastAPI(
    title="Product Catalog API",
    description="A simple API to manage items",
    version="1.0.0"
)
# app = FastAPI()

app.include_router(item_router)
