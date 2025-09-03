from sqlalchemy.orm import Session
from app.models.like import Like

def toggle_like(db: Session, user_id: int, tweet_id: int):
    like = db.query(Like).filter_by(user_id=user_id, tweet_id=tweet_id, is_retweet=False).first()
    if like:
        db.delete(like)
        db.commit()
        return {"liked": False}
    new_like = Like(user_id=user_id, tweet_id=tweet_id)
    db.add(new_like)
    db.commit()
    db.refresh(new_like)
    return {"liked": True}

def toggle_retweet(db: Session, user_id: int, tweet_id: int):
    retweet = db.query(Like).filter_by(user_id=user_id, tweet_id=tweet_id, is_retweet=True).first()
    if retweet:
        db.delete(retweet)
        db.commit()
        return {"retweeted": False}
    new_retweet = Like(user_id=user_id, tweet_id=tweet_id, is_retweet=True)
    db.add(new_retweet)
    db.commit()
    db.refresh(new_retweet)
    return {"retweeted": True}
