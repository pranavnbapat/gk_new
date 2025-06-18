# app/models/auth.py

import uuid

from sqlalchemy import Column, Integer, String, Boolean, DateTime, SmallInteger
from sqlalchemy.sql import func
from sqlalchemy_continuum import make_versioned

from app.db.base import Base

# Enable versioning globally
make_versioned(user_cls=None)


class AuthUserExtend(Base):
    __versioned__ = {}
    __tablename__ = "auth_user_extend"

    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    email = Column(String(254), unique=True, nullable=False)
    username = Column(String(150), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    contact_no = Column(String(10), index=True)
    token_version = Column(Integer, default=1)

    is_active = Column(Boolean, default=True, nullable=False)
    is_staff = Column(Boolean, default=False, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    last_login = Column(DateTime)
    date_joined = Column(DateTime, default=func.now(), nullable=False)

    status = Column(SmallInteger, default=1)
    deleted_at = Column(DateTime)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
