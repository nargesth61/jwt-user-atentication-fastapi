from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import  schemas
from app.crud import crud_user,oauth2
from app.database import get_db
from app.services.tasks import send_email_task
from app.models.user import User
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()

@router.post("/register", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    otp_code = crud_user.create_otp_code()
    user = crud_user.create_user(db=db, user=user, otp_code=otp_code)
    
    new_profile = crud_user.create_profile(db=db,user_id=user.id, first_name=None, last_name=None) 
    db.add(new_profile)
    db.commit()

    send_email_task.delay(user.email, otp_code)
    
    return user

@router.post("/verify-otp")
def verify_otp_route(
    user_email: str, 
    otp_code: str, 
    db: Session = Depends(get_db)
):
    result = crud_user.verify_otp(db=db, user_email=user_email, otp_code=otp_code)

    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    
    return {"message": result["message"]}

@router.post("/login")
def login_user(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, email=user.email)
    if db_user is None:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    if not db_user.is_verified:
        raise HTTPException(status_code=400, detail="Please verify your email before logging in")
    
    access_token = oauth2.create_access_token(data={"sub": db_user.email,"id": db_user.id})
    return {"access_token": access_token, "token_type": "bearer"}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/logout")
def logout(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    # بررسی اینکه آیا توکن قبلاً در لیست سیاه قرار دارد
    if crud_user.is_token_blacklisted(db, token):
        raise HTTPException(status_code=401, detail="Token has already been logged out")

    # توکن را به لیست سیاه اضافه می‌کنیم
    crud_user.add_token_to_blacklist(db, token)

    return {"message": "Successfully logged out"}