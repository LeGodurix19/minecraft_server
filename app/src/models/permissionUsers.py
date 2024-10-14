from sqlalchemy import Column, Integer, String, BigInteger, Text, DateTime, func
from .base import Base

class PermissionUser(Base):
    __tablename__ = 'permission_users'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(BigInteger, index=True)
    permission = Column(Integer, index=True)
    
    
# Permissions list
# 0: Default
# 1: Moderator
# 2: Admin
# 3: Owner