from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from ..config import JWT_SECRET, JWT_ALG, JWT_EXP_MIN


pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    
    return pwd_ctx.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
    
    return pwd_ctx.verify(password, password_hash)


def create_access_token(sub: str) -> str:
    
    exp = datetime.utcnow() + timedelta(minutes=JWT_EXP_MIN)
    
    payload = {"sub": sub, "exp": exp}
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALG)