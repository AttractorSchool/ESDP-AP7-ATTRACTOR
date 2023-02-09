# from django.views.generic import ListView
# from datetime import datetime
# from calendarapp.models import Event
#
#
# class AllEventsListView(ListView):
#     """ All event list views """
#
#     template_name = "calendarapp/events_list.html"
#     model = Event
#
#     def get_queryset(self):
#         return Event.objects.get_all_events(user=self.request.user)
#
#
# class RunningEventsListView(ListView):
#     """ Running events list view """
#
#     template_name = "calendarapp/events_list.html"
#     model = Event
#
#     def get_queryset(self):
#         return Event.objects.get_running_events(user=self.request.user)
#
#
# class ActualEventsListView(ListView):
#     """ Running events list view """
#
#     template_name = "calendarapp/events_list.html"
#     model = Event
#
#     def get_queryset(self):
#         print(datetime.now().date())
#         return Event.objects.filter(user=self.request.user, start_time__gte=datetime.now())
