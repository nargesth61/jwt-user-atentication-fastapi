from sqlalchemy.orm import Session
from app.models.user import User,BlacklistedToken
from app.models.profile import Profile
from app.schemas import UserCreate, UserUpdate
import random
import string
from passlib.context import CryptContext
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_profile(db: Session, user_id: int, first_name: str, last_name: str):
    new_profile = Profile(user_id=user_id, first_name=first_name, last_name=last_name)
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    return new_profile

def create_user(db: Session, user: UserCreate, otp_code: str):
    hashed_password = hash_password(user.hashed_password)
    otp_expiration = datetime.now() + timedelta(minutes=3)

    db_user = User(email=user.email, hashed_password=hashed_password ,is_active=True, otp_code=otp_code,otp_expiration=otp_expiration)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_otp_code() -> str:
    return ''.join(random.choices(string.digits, k=6))

def verify_otp(db: Session, user_email: str, otp_code: str):
    db_user = db.query(User).filter(User.email == user_email).first()
    
    if db_user is None:
        return {"error": "User not found"}
    
    if db_user.otp_expiration < datetime.now():
        return {"error": "OTP expired"}
    
    if db_user.otp_code != otp_code:
        return {"error": "Invalid OTP"}
   
    db_user.otp_code = None  
    db_user.otp_expiration = None  
    db_user.is_verified =True
    db.commit()
    return {"message": "OTP verified successfully"}

def update_user(db: Session, user_id: int, profile: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        if profile.first_name:
            db_user.profile.first_name = profile.first_name
        if profile.last_name:
            db_user.profile.last_name = profile.last_name
        db.commit()
        db.refresh(db_user)
    return db_user

def add_token_to_blacklist(db: Session, token: str):
    db_token = BlacklistedToken(token=token)
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    return db_token

def is_token_blacklisted(db: Session, token: str) -> bool:
    db_token = db.query(BlacklistedToken).filter(BlacklistedToken.token == token).first()
    return db_token is not None