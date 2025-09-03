from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func,Text
from sqlalchemy.orm import relationship
from app.db.base import Base

class Tweet(Base):
    __tablename__ = "tweets"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    created_at = Column(DateTime, server_default=func.now())

    # relationships
    owner = relationship("User", back_populates="tweets")
    comments = relationship("Comment", back_populates="tweet", cascade="all, delete-orphan")
    # likes = relationship("Like", back_populates="tweet", cascade="all, delete-orphan")
    # hashtags = relationship("Hashtag", secondary="tweet_hashtags", back_populates="tweets")
