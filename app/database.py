# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy_continuum import make_versioned, versioning_manager

from app.config import settings
from app.models.versioning import Transaction


DATABASE_URL = (
    f"mysql+pymysql://{settings.DB_USER}:{settings.DB_PASS}"
    f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
)

# Create SQLAlchemy engine and session
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Register the Transaction class for MySQL compatibility
versioning_manager.transaction_cls = Transaction

# Globally enables versioning
make_versioned(user_cls=None)


# DATABASE_URL = "sqlite:///./gatekeeper.db"
# engine = create_engine(
#     DATABASE_URL, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# versioning_manager.transaction_cls = Transaction
# make_versioned(user_cls=None)
