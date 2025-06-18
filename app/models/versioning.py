# app/models/versioning.py

from sqlalchemy import Column, Integer, DateTime, String
from app.db.base import Base

class Transaction(Base):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True, autoincrement=True)
    issued_at = Column(DateTime)
    remote_addr = Column(String(100))
