from sqlalchemy import Column, Integer, String, DateTime, Float
from src.db.base import Base
from datetime import datetime


class WalletQuery(Base):
    __tablename__ = "wallet_queries"

    id = Column(Integer, primary_key=True)
    address = Column(String)
    balance = Column(Float)
    bandwidth = Column(Integer)
    energy = Column(Integer)
