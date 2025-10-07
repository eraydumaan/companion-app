from pydantic import BaseModel, EmailStr
from typing import Optional


# --- Kullanıcı oluşturma ---
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str


# --- Giriş (login) ---
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# --- Kullanıcı genel görünümü ---
class UserPublic(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    city: Optional[str] = None
    is_partner: bool
    hourly_rate: Optional[int] = None
    bio: Optional[str] = None

    class Config:
        from_attributes = True  # SQLAlchemy -> Pydantic dönüşümü


# --- Kullanıcı bilgilerini güncelleme ---
class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    city: Optional[str] = None
    is_partner: Optional[bool] = None
    hourly_rate: Optional[int] = None
    bio: Optional[str] = None

    class Config:
        from_attributes = True


# --- Token modeli ---
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
