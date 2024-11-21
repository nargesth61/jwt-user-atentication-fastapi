from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from app.crud.s3_utils import upload_image_to_s3
from app.models.avatar import UserProfileImage
from app.database import get_db
from app.crud.oauth2 import get_current_user
from datetime import datetime

router = APIRouter()

@router.post("/upload")
def upload_profile_image(image: UploadFile = File(...), db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    user_id = current_user.get("id")
    
    try:
        image_url = upload_image_to_s3(image, user_id)
        
        db_image = UserProfileImage(user_id=user_id, image_url=image_url, upload_date=str(datetime.now()))
        db.add(db_image)
        db.commit()
        
        return {"message": "Image uploaded successfully", "image_url": image_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))