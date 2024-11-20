from fastapi_mail import FastMail, MessageSchema
from app.settings import MAIL_USERNAME, MAIL_PASSWORD, MAIL_SERVER, MAIL_PORT, MAIL_BACKEND, MAIL_FROM
from fastapi_mail.config import ConnectionConfig
import logging
from app.settings import CELERY_BROKER_URL, CELERY_RESULT_BACKEND
from app.celery_worker import celery
from celery import shared_task

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Setting FastAPI-Mail
mail_config = ConnectionConfig(
    MAIL_USERNAME=MAIL_USERNAME,
    MAIL_PASSWORD=MAIL_PASSWORD,
    MAIL_SERVER=MAIL_SERVER,
    MAIL_PORT=MAIL_PORT,
    MAIL_FROM=MAIL_FROM,
    
)

# Task Send Email
@shared_task
def send_email_task(email: str, otp_code: str):
    fm = FastMail(mail_config)
    message = MessageSchema(
        subject="تأیید ایمیل",
        recipients=[email],
        body=f"Your OTP code is: {otp_code}",
        subtype="html"
    )
    logger.info(f"Sending email to {email} with code {otp_code}")
    fm.send_message(message)
    