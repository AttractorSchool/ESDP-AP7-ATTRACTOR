from datetime import datetime
from django.db import models

from django.shortcuts import redirect
from django.urls import reverse

from calendarapp.models import EventAbstract
from accounts.models import Account
from calendarapp.models.event_format import EventFormat


class EventManager(models.Manager):
    """ Event manager """

    def get_all_events(self, user):
        if user.type == 'tutor':
            events = Event.objects.filter(user=user, is_active=True, is_deleted=False)

        if user.type == 'student':
            eventmembers = EventMember.objects.filter(user=user)
            events = Event.objects.filter(events__in=eventmembers)

        if user.type == 'parents':
            parent = Account.objects.get(id=user.pk)
            children = Account.objects.filter(is_deleted=False, parent_id=parent.pk).values('id', 'survey')
            children_pk_list = [child.get('id') for child in children]
            eventmembers = EventMember.objects.filter(user__in=children_pk_list)
            events = Event.objects.filter(events__in=eventmembers)

        return events

    def get_running_events(self, user):
        if user.type == 'tutor':
            running_events = Event.objects.filter(
                user=user,
                is_active=True,
                is_deleted=False,
                end_time__gte=datetime.now().date(),
            ).order_by("start_time")

        if user.type == 'student':
            eventmembers = EventMember.objects.filter(user=user)
            running_events = Event.objects.filter(
                events__in=eventmembers, is_active=True,
                is_deleted=False,
                end_time__gte=datetime.now().date(),
            ).order_by("start_time")

        if user.type == 'parents':
            children = Account.objects.filter(is_deleted=False, parent_id=user.pk).values('id', 'survey')
            children_pk_list = [child.get('id') for child in children]
            eventmembers = EventMember.objects.filter(user__in=children_pk_list)

            running_events = Event.objects.filter(
                events__in=eventmembers, is_active=True,
                is_deleted=False,
                end_time__gte=datetime.now().date(),
            ).order_by("start_time")

        return running_events

    def get_today_events(self, user):
        events_today = Event.objects.filter(
            user=user,
            is_active=True,
            is_deleted=False,
            start_time__date=datetime.now().date(),
        ).order_by("start_time")
        return events_today


class Event(EventAbstract):
    """ Event model """

    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="events")
    title = models.CharField(max_length=200, unique=False)
    description = models.TextField()
    event_format = models.ForeignKey( to='calendarapp.EventFormat',
                                      null=True,
                                      on_delete=models.CASCADE,
                                      related_name="events")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    objects = EventManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("calendarapp:calendar")


    @property
    def get_html_url(self):
        url = reverse("calendarapp:event-detail", args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'


class EventMember(EventAbstract):
    """ Event member model """

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="events")
    user = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="event_members"
    )

    class Meta:
        unique_together = ["event", "user"]

    def __str__(self):
        return str(self.user)