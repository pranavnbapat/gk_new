# app/auth/jwt.py

from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from app.config import settings

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.JWT_SIGNING_KEY, algorithm=settings.JWT_ALG)

def create_refresh_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.JWT_SIGNING_KEY, algorithm=settings.JWT_ALG)

def validate_token(token: str, token_type: str = "access"):
    try:
        payload = jwt.decode(token, settings.JWT_SIGNING_KEY, algorithms=[settings.JWT_ALG])
        exp = payload.get("exp")
        if not exp:
            raise ValueError("Missing expiration")
        now = datetime.now(timezone.utc).timestamp()
        if exp < now:
            return False, "Token has expired"
        return True, exp - now
    except JWTError:
        return False, "Invalid token"
