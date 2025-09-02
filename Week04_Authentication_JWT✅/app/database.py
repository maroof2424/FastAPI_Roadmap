from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./auth.db"

# Create engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a configured "SessionLocal" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our ORM models
Base = declarative_base()

# Dependency for DB session (to be used in routes)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
