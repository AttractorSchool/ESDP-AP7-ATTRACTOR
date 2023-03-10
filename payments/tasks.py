from django.utils import timezone

from .models import ServiceStatus
from enimi.celery import app

@app.task
def update_service_status():
    services = list(ServiceStatus.objects.filter(
        status='1',
        end_date__lt=timezone.now()))
    for service in services:
        service.status = '0'
        service.save()
    return services
