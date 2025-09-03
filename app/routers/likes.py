from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.crud import like as like_crud
from app.routers.auth import get_current_user
from app.crud import user as user_crud

router = APIRouter(prefix="/likes", tags=["Likes"])

@router.post("/like/{tweet_id}")
def like_tweet(tweet_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    user = user_crud.get_by_username(db, current_user)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return like_crud.toggle_like(db, user.id, tweet_id)

@router.post("/retweet/{tweet_id}")
def retweet(tweet_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    user = user_crud.get_by_username(db, current_user)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return like_crud.toggle_retweet(db, user.id, tweet_id)
