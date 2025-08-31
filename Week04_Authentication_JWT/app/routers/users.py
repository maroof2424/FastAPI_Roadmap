from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import SessionLocal
from app.utils import hash_password
from app.dependencies import get_current_user   # ✅ Fix 1

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if email already exists
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash password
    hashed_pw = hash_password(user.password)
    new_user = models.User(
        username=user.username,
        email=user.email,
        password=hashed_pw
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/me", response_model=schemas.UserOut)
def read_current_user(current_user: models.User = Depends(get_current_user)):   # ✅ Fix 2
    return current_user
