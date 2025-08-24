from sqlalchemy.orm import Session
from app import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    new_user = models.User(username=user.username, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session):
    return db.query(models.User).all()


def create_post(db: Session, post: schemas.PostCreate):
    new_post = models.Post(title=post.title, content=post.content, author_id=post.author_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_posts(db: Session):
    return db.query(models.Post).all()
