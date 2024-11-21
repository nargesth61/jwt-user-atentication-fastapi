from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    hashed_password: str

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None

class User(UserBase):
    id: int
    is_active: bool
    is_verified: bool

    class Config:
        orm_mode = True

class Profile(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None

    class Config:
        orm_mode = True
    
class UserLogin(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True

class UserEmail(BaseModel):
    email: EmailStr