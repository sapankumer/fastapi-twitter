from sqlalchemy.orm import Session
from app.models.tweet import Tweet
from app.schemas.tweet import TweetCreate

def create(db: Session, user_id: int, payload: TweetCreate) -> Tweet:
    tweet = Tweet(content=payload.content, user_id=user_id)
    db.add(tweet)
    db.commit()
    db.refresh(tweet)
    return tweet

def get_all(db: Session):
    return db.query(Tweet).order_by(Tweet.created_at.desc()).all()

def get_by_id(db: Session, tweet_id: int):
    return db.query(Tweet).filter(Tweet.id == tweet_id).first()

def delete(db: Session, tweet_id: int, user_id: int):
    tweet = get_by_id(db, tweet_id)
    if tweet and tweet.user_id == user_id:
        db.delete(tweet)
        db.commit()
        return True
    return False
