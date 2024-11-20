from sqlalchemy import Column, Integer, String, Boolean,DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy.orm import declarative_base
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    otp_code = Column(String, nullable=True)
    otp_expiration = Column(DateTime, index=True)

    profile = relationship("Profile", back_populates="user", uselist=False)

class BlacklistedToken(Base):
    __tablename__ = "blacklisted_tokens"
    
    token = Column(String, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)