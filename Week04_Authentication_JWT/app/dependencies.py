from app.database import SessionLocal
from app.auth import get_current_user

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# re-export get_current_user
get_current_user = get_current_user
