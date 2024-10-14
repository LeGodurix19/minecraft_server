from sqlalchemy import Column, Integer, String, BigInteger, Text, DateTime, func
from .base import Base

class SyncUser(Base):
    __tablename__ = 'sync_users'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(BigInteger, index=True)
    username = Column(String, index=True)
    minecraft_username = Column(String, index=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    