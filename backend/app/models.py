from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from .database import Base


class User(Base):
    __tablename__ = "users"


id = Column(Integer, primary_key=True, index=True)
email = Column(String(255), unique=True, index=True, nullable=False)
password_hash = Column(String(255), nullable=False)
full_name = Column(String(255), nullable=False)
city = Column(String(100))
is_partner = Column(Boolean, default=False, nullable=False)
hourly_rate = Column(Integer)
bio = Column(String(1000))
created_at = Column(DateTime(timezone=True), server_default=func.now())
updated_at = Column(DateTime(timezone=True), onupdate=func.now())