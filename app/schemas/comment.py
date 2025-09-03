from typing import Optional

from pydantic import BaseModel
from datetime import datetime

class CommentCreate(BaseModel):
    comment: str
    tweet_id: int

class CommentResponse(BaseModel):
    id: int
    comment: str
    user_id: int
    tweet_id: Optional[int] = None
    created_at: datetime

    class Config:
        from_attributes = True
