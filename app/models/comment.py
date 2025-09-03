from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base

class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)
    comment = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    tweet_id = Column(Integer, ForeignKey("tweets.id", ondelete="CASCADE"))
    created_at = Column(DateTime, default=datetime.utcnow)
    # relationships
    user = relationship("User", back_populates="comments")
    tweet = relationship("Tweet", back_populates="comments")