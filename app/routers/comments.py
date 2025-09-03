from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.schemas.comment import CommentCreate, CommentResponse
from app.db.session import get_db
from app.crud import comment as comment_crud
from typing import List

router = APIRouter(prefix="/comments", tags=["Comments"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")
from app.routers.auth import get_current_user

@router.post("/", response_model=CommentResponse)
def create_comment(payload: CommentCreate, db: Session = Depends(get_db), current_username: str =Depends(get_current_user)):
    from app.crud import user as user_crud
    user = user_crud.get_by_username(db, current_username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return comment_crud.create_comment(db, user.id, payload)

@router.get("/", response_model=List[CommentResponse], dependencies=[])
def list_comment(db: Session = Depends(get_db)):
    return comment_crud.get_all(db)

