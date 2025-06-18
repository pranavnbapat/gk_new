# scripts/create_superuser.py

from getpass import getpass
from app.database import SessionLocal
from app.models.auth import AuthUserExtend
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_superuser():
    db = SessionLocal()

    username = input("Username: ")
    email = input("Email: ")
    password = getpass("Password: ")

    hashed_password = pwd_context.hash(password)

    existing = db.query(AuthUserExtend).filter(
        (AuthUserExtend.username == username) | (AuthUserExtend.email == email)
    ).first()

    if existing:
        print("❌ User already exists.")
        return

    user = AuthUserExtend(
        username=username,
        email=email,
        password=hashed_password,
        first_name="Admin",
        last_name="User",
        is_active=True,
        is_superuser=True,
        is_staff=True
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    print(f"✅ Superuser '{username}' created with ID {user.id}")

if __name__ == "__main__":
    create_superuser()
