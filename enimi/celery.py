import os
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'enimi.settings')

app = Celery('enimi')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'update_service_status_beat': {
        'task': 'payments.tasks.update_service_status',
       # 'schedule': timedelta(seconds=30),
        'schedule': crontab(hour=0, minute=1)
    },
}

app.conf.timezone = 'Asia/Almaty'
