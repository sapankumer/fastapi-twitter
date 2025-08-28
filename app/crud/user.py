from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.user import User
from app.core.security import hash_password, verify_password


def get_by_username(db: Session, username: str) -> User | None:
    return db.scalar(select(User).where(User.username == username))


def get_by_email(db: Session, email: str) -> User | None:
    return db.scalar(select(User).where(User.email == email))


def create(db: Session, username: str, email: str, full_name: str, password: str, is_active: bool = True) -> User:
    u = User(username=username, email=email, full_name=full_name, hashed_password=hash_password(password),
             is_active=is_active)
    db.add(u)
    db.commit()
    db.refresh(u)
    return u


def authenticate(db: Session, username: str, password: str) -> User | None:
    u = get_by_username(db, username)
    if not u:
        return None
    if not verify_password(password, u.hashed_password):
        return None
    return u
