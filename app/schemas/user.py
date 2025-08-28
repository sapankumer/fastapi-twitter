from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


# Shared properties
class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    is_active: Optional[bool] = True


# Create user request schema
class UserCreate(UserBase):
    password: str


# Update user request schema
class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None


# Response schema (exclude password)
class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


# Login request schema
class UserLogin(BaseModel):
    username: str
    password: str


# Token schema
class Token(BaseModel):
    access_token: str
    token_type: str = "Bearer"


class TokenData(BaseModel):
    username: Optional[str] = None
