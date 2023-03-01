from django.contrib import admin
from calendarapp import models


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    model = models.Event
    list_display = [
        "id", "title", "user", "is_active", "is_deleted", "created_at", "updated_at",
        "description", "start_time", "end_time", "user_id", "event_format"
    ]
    list_filter = ["is_active", "is_deleted"]
    search_fields = ["title"]

@admin.register(models.EventFormat)
class EventFormat(admin.ModelAdmin):
    model = models.EventFormat
    list_display = ["id", "format_name", "created_at", "updated_at"]
    list_filter = ["format_name"]

@admin.register(models.EventMember)
class EventMemberAdmin(admin.ModelAdmin):
    model = models.EventMember
    list_display = ["id", "event", "user", "created_at", "updated_at"]
    list_filter = ["event"]
