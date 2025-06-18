# app/auth/services.py

from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import AuthUserExtend
from app.auth.jwt import create_access_token, create_refresh_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_user(username: str, password: str):
    db: Session = SessionLocal()
    try:
        user = db.query(AuthUserExtend).filter(
            (AuthUserExtend.username == username) |
            (AuthUserExtend.email == username)
        ).first()

        if not user:
            return None

        if not pwd_context.verify(password, user.password):
            return None

        return user
    finally:
        db.close()


def login_user(username: str, password: str):
    """
    Uses the above DB query to create JWT access and refresh tokens.
    """
    user = verify_user(username, password)

    payload = {
        "uuid": str(user.uuid),
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name
    }

    access_token = create_access_token(payload)
    refresh_token = create_refresh_token(payload)

    return {
        "success": True,
        "access": access_token,
        "refresh": refresh_token
    }
