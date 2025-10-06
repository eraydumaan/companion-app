from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    city: Optional[str] = None
    is_partner: bool
    hourly_rate: Optional[int] = None
    bio: Optional[str] = None


class Config:
    from_attributes = True


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    city: Optional[str] = None
    is_partner: Optional[bool] = None
    hourly_rate: Optional[int] = None
    bio: Optional[str] = None


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"