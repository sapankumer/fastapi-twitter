from sqlalchemy.orm import Session
from app.models.comment import Comment
from app.schemas.comment import CommentCreate


def create_comment(db: Session, user_id: int, payload: CommentCreate) -> Comment:
    comment = Comment(comment=payload.comment, user_id=user_id, tweet_id=payload.tweet_id)
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment

def get_all(db: Session):
    return db.query(Comment).order_by(Comment.created_at.desc()).all()

def get_comments_by_tweet(db: Session, tweet_id: int):
    return db.query(Comment).filter(Comment.tweet_id == tweet_id).all()
