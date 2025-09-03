from sqlalchemy import Column, Integer, ForeignKey, Boolean
from app.db.base import Base

class Like(Base):
    __tablename__ = "likes"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    tweet_id = Column(Integer, ForeignKey("tweets.id", ondelete="CASCADE"))
    is_retweet = Column(Boolean, default=False)
