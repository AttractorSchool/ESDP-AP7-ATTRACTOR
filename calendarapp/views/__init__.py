# from .event_list import AllEventsListView, RunningEventsListView, ActualEventsListView

from .other_views import (
    CalendarViewNew,
    CalendarView,
    create_event,
    EventEdit,
    event_details,
    add_eventmember,
    EventMemberDeleteView,
    EventDeleteView,
AllEventsListView, RunningEventsListView, ActualEventsListView

)


__all__ = [
    AllEventsListView,
    RunningEventsListView,
    CalendarViewNew,
    CalendarView,
    create_event,
    EventEdit,
    event_details,
    add_eventmember,
    EventMemberDeleteView,
    EventDeleteView,
    ActualEventsListView,
]
