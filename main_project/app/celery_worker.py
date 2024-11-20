from celery import Celery
from app.settings import CELERY_BROKER_URL, CELERY_RESULT_BACKEND


celery = Celery(
    "email_service",
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND,
)

celery.conf.update(
    result_expires=3600,
    task_serializer='json',
    result_serializer='json',
    accept_content=['json'],
    timezone='UTC',
    enable_utc=True,
)
celery.config_from_object('app.services.tasks')