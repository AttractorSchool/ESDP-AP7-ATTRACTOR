from django.shortcuts import redirect, render
from django.utils.safestring import mark_safe
from datetime import timedelta, datetime, date
import calendar

from django.views.generic import ListView

from calendarapp.forms import EventForm
from calendarapp.models import EventMember, Event
from calendarapp.utils import Calendar

class MainPageScheduleView(ListView):
    model = Event
    template_name = "tutor_cabinet_main_page.html"
    form_class = EventForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        events = Event.objects.get_all_events(user=request.user)

        eventmembers = EventMember.objects.all()

        events_month = Event.objects.get_running_events(user=request.user)
        events_today = Event.objects.get_today_events(user=request.user)
        event_list = []
        # start: '2020-09-16T16:00:00'
        for event in events:
            event_list.append(
                {
                    "title": event.title,
                    "start": event.start_time.strftime("%Y-%m-%dT%H:%M:%S"),
                    "end": event.end_time.strftime("%Y-%m-%dT%H:%M:%S"),

                }
            )
        counter = 1
        context = {"form": forms, "events": event_list, "counter": counter,
                   "events_month": events_month, "eventmembers": eventmembers,
                   "events_today": events_today}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            form = forms.save(commit=False)
            form.user = request.user
            form.save()
            return redirect("calendarapp:calendar")
        context = {"form": forms}
        return render(request, self.template_name, context)