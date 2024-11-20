from app.models.profile import Profile 
from app.database import get_db 
from app.crud.oauth2 import get_current_user  
from fastapi import Depends,APIRouter,HTTPException
from sqlalchemy.orm import Session
from app import schemas

router = APIRouter()

@router.get("/")
def get_profile(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    user_id = current_user.get("id") 
    profile = db.query(Profile).filter(Profile.user_id == user_id).first()  
    if not profile:
        return {"message": "Profile not found"}  
    return {
        "first_name": profile.first_name,
        "last_name": profile.last_name,
        "email": current_user.get("sub")  
    }

@router.put("/edit/profile", response_model=schemas.Profile)
def update_profile(
    profile_update: schemas.Profile,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    user_id = current_user.get("id")
    
    profile = db.query(Profile).filter(Profile.user_id == user_id).first()  
    
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    
    if profile_update.first_name:
        profile.first_name = profile_update.first_name
    if profile_update.last_name:
        profile.last_name = profile_update.last_name
    
    db.commit()
    db.refresh(profile)
    
    return profile