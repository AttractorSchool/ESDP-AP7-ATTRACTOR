# cal/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import timedelta, datetime, date
import calendar
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView

from accounts.models import Account
from cabinet_tutors.models import MyStudent
from calendarapp.models import Event, EventMember

from calendarapp.utils import Calendar
from calendarapp.forms import EventForm, AddMemberForm
from ratings.forms import MemberEventRatingForm
from ratings.models import MemberEventRating


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split("-"))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = "month=" + str(prev_month.year) + "-" + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = "month=" + str(next_month.year) + "-" + str(next_month.month)
    return month


class CalendarView(LoginRequiredMixin, generic.ListView):
    login_url = "accounts:signin"
    model = Event
    template_name = "calendar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get("month", None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context["calendar"] = mark_safe(html_cal)
        context["prev_month"] = prev_month(d)
        context["next_month"] = next_month(d)
        return context


@login_required(login_url="signup")
def create_event(request):
    form = EventForm(request.POST or None)
    if request.POST and form.is_valid():
        title = form.cleaned_data["title"]
        description = form.cleaned_data["description"]
        event_form = form.cleaned_data["event_form"]
        start_time = form.cleaned_data["start_time"]
        end_time = form.cleaned_data["end_time"]
        Event.objects.get_or_create(
            user=request.user,
            title=title,
            description=description,
            event_form=event_form,
            start_time=start_time,
            end_time=end_time,
        )
        return HttpResponseRedirect(reverse("calendarapp:calendar"))
    return render(request, "event.html", {"form": form})


class EventEdit(LoginRequiredMixin,generic.UpdateView):
    model = Event
    # fields = ["title", "description", "start_time", "end_time"]
    template_name = "event.html"
    form_class = EventForm




@login_required(login_url="signup")
def event_details(request, event_id):
    event = Event.objects.get(id=event_id)
    eventmember = EventMember.objects.filter(event=event)
    event_member_ratings = MemberEventRating.objects.filter(event=event)
    context = {"event": event, "eventmember": eventmember, "back_page": request.META.get('HTTP_REFERER'),
               "rate_form": MemberEventRatingForm, "event_member_ratings": event_member_ratings}
    return render(request, "event-details.html", context)

@login_required(login_url="signup")
def add_eventmember(request, event_id):
    print(request.user)
    context = {}
    forms = AddMemberForm(current_user=request.user)
    if request.method == "POST":
        # forms = AddMemberForm(request.POST)
        # if forms.is_valid():

        # member = EventMember.objects.filter(event=event_id)
        event = Event.objects.get(id=event_id)

        # user = forms.cleaned_data["user"]
        tutor_student_id = request.POST['user']
        tutor_student = MyStudent.objects.get(id=tutor_student_id)
        user = Account.objects.get(id=tutor_student.student.pk)

        in_table = EventMember.objects.filter(event=event, user=user)
        if not in_table:
            # EventMember.objects.create(event=event, user=user)
            event_member = EventMember.objects.create(event=event, user=user)
            print(event_member)
            # event_member.student.add(tutor_student.student)
            event_member.save()
            context = {"form": forms}
            context['ok'] = 'Ученик добавлен'
            return render(request, "add_member.html", context)
        else:
            context = {"form": forms}
            context['error'] = 'Вы уже добавили этого ученика'
            return render(request, "add_member.html", context)
    context = {"form": forms}
    return render(request, "add_member.html", context)


class EventMemberDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = EventMember
    template_name = "event_delete.html"
    success_url = reverse_lazy("calendarapp:calendar")


class EventDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Event
    template_name = "event_delete.html"
    success_url = reverse_lazy("calendarapp:calendar")


class CalendarViewNew(LoginRequiredMixin, generic.View):
    login_url = "accounts:signin"
    template_name = "calendarapp/calendar.html"
    form_class = EventForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        if request.user.type == 'tutor':
            user = Account.objects.get(id=request.user.pk)
            events = Event.objects.get_all_events(user=user)
            eventmembers = EventMember.objects.all()
            events_month = Event.objects.get_running_events(user=request.user)
            event_list = []
            # start: '2020-09-16T16:00:00'

        if request.user.type == 'student':
            user = Account.objects.get(id=request.user.pk)
            eventmembers = EventMember.objects.filter(user=user)
            events = Event.objects.filter(events__in=eventmembers)
            events_month = Event.objects.get_running_events(user=request.user)
            event_list = []

        if request.user.type == 'parents':
            parent = Account.objects.get(id=request.user.pk)
            children = Account.objects.filter(is_deleted=False, parent_id=parent.pk).values('id', 'survey')
            children_pk_list = [child.get('id') for child in children]
            eventmembers = EventMember.objects.filter(user__in=children_pk_list)
            events = Event.objects.filter(events__in=eventmembers)
            events_month = Event.objects.get_running_events(user=request.user)
            event_list = []

        for event in events:
            event_list.append(
                {
                    "title": event.title,
                    "start": event.start_time.strftime("%Y-%m-%dT%H:%M:%S"),
                    "end": event.end_time.strftime("%Y-%m-%dT%H:%M:%S"),

                }
            )
        context = {"form": forms, "events": event_list,
                   "events_month": events_month, "eventmembers": eventmembers}
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



class AllEventsListView(LoginRequiredMixin,ListView):
    """ All event list views """

    template_name = "calendarapp/events_list.html"
    model = Event

    def get_queryset(self):
        return Event.objects.get_all_events(user=self.request.user)


class RunningEventsListView(LoginRequiredMixin,ListView):
    """ Running events list view """

    template_name = "calendarapp/events_list.html"
    model = Event

    def get_queryset(self):
        return Event.objects.get_running_events(user=self.request.user)


class ActualEventsListView(LoginRequiredMixin,ListView):
    """ Running events list view """

    template_name = "calendarapp/events_list.html"
    model = Event

    def get_queryset(self):
        # print(datetime.now().date())
        if self.request.user.type == 'tutor':
            return Event.objects.filter(user=self.request.user, start_time__gte=datetime.now())

        if self.request.user.type == 'student':
            user = Account.objects.get(id=self.request.user.pk)
            eventmembers = EventMember.objects.filter(user=user)
            return Event.objects.filter(events__in=eventmembers, start_time__gte=datetime.now())

        if self.request.user.type == 'parents':
            parent = Account.objects.get(id=self.request.user.pk)
            children = Account.objects.filter(is_deleted=False, parent_id=parent.pk).values('id', 'survey')
            children_pk_list = [child.get('id') for child in children]
            eventmembers = EventMember.objects.filter(user__in=children_pk_list)
            return Event.objects.filter(events__in=eventmembers, start_time__gte=datetime.now())
