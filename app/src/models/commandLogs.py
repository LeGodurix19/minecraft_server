from sqlalchemy import Column, Integer, String, BigInteger, Text, DateTime, func
from .base import Base

class CommandLog(Base):
    __tablename__ = 'command_logs'

    id = Column(Integer, primary_key=True, index=True)
    command = Column(String, index=True)
    arguments = Column(Text, nullable=True)
    user_id = Column(BigInteger, index=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    