from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.schemas.tweet import TweetCreate, TweetResponse
from app.crud import tweet as tweet_crud
from app.core.security import decode_token
from fastapi.security import OAuth2PasswordBearer


router = APIRouter(prefix="/tweets", tags=["Tweets"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")
from app.routers.auth import get_current_user

@router.post("/", response_model=TweetResponse)
def create_tweet(payload: TweetCreate, db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    from app.crud import user as user_crud
    user = user_crud.get_by_username(db, username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return tweet_crud.create(db, user.id, payload)

@router.get("/", response_model=List[TweetResponse], dependencies=[])
def list_tweets(db: Session = Depends(get_db)):
    return tweet_crud.get_all(db)

@router.delete("/{tweet_id}")
def delete_tweet(tweet_id: int, db: Session = Depends(get_db), username: str = Depends(get_current_user)):
    from app.crud import user as user_crud
    user = user_crud.get_by_username(db, username)
    if not tweet_crud.delete(db, tweet_id, user.id):
        raise HTTPException(status_code=403, detail="Not authorized or tweet not found")
    return {"message": "Tweet deleted successfully"}
