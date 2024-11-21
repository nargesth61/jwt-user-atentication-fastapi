from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class UserProfileImage(Base):
    __tablename__ = "user_profile_images"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    image_url = Column(String, nullable=False)  
    upload_date = Column(String, nullable=False)  
    
    user = relationship("User", back_populates="profile_image")