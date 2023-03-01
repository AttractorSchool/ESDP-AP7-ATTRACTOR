from django.contrib import admin

from payments.models.orders import Order
from payments.models.services import Service
from payments.models.services_status import ServiceStatus


class OrderAdmin(admin.ModelAdmin):
    list_display = ['email', 'amount', 'description', 'created_at', 'status', 'service', 'user']


admin.site.register(Order, OrderAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'duration']


admin.site.register(Service, ServiceAdmin)


class ServiceStatusAdmin(admin.ModelAdmin):
    list_display = ['user', 'service', 'start_date', 'end_date', 'status']


admin.site.register(ServiceStatus, ServiceStatusAdmin)