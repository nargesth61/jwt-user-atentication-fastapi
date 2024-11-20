from dotenv import load_dotenv
import os

# .env loader
load_dotenv()

# Setting PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL")

# Setting JWT
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

# Setting Email

MAIL_USERNAME = os.getenv("MAIL_USERNAME")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
MAIL_SERVER = os.getenv("MAIL_SERVER")
MAIL_PORT = os.getenv("MAIL_PORT")
MAIL_FROM = os.getenv("MAIL_FROM")

MAIL_BACKEND = os.getenv("MAIL_BACKEND")

# Setting Celery
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")