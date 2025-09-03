from pydantic import BaseModel
from datetime import datetime

class TweetBase(BaseModel):
    content: str

class TweetCreate(TweetBase):
    pass

class TweetResponse(TweetBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True
