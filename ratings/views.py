from django.http import JsonResponse
from django.views.generic import CreateView

from accounts.models import Account
from calendarapp.models import Event, EventMember
from ratings.models import MemberEventRating


class RateCreateView(CreateView):
    model = MemberEventRating

    def post(self, request, *args, **kwargs):
        event = Event.objects.get(id=kwargs.get('event_id'))
        event_member = EventMember.objects.get(id=kwargs.get('member_id'))
        in_table = MemberEventRating.objects.filter(event=event, event_member=event_member)
        if in_table:
            in_table = MemberEventRating.objects.get(event=event, event_member=event_member)
            in_table.score = request.POST['score']
            in_table.comment = request.POST['comment']
            member_rate = in_table

        else:
            member_rate = MemberEventRating.objects.create(event=event, event_member=event_member,
                                         score=request.POST['score'], comment=request.POST['comment'])
        member_rate.save()
        rate = member_rate.score
        answer = {}
        answer['rate'] = rate
        return JsonResponse(answer)