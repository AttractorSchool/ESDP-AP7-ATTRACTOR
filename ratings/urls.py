from django.urls import path

from ratings.views import RateCreateView

urlpatterns = [
    path('create/event_member/<int:member_id>/event/<int:event_id>', RateCreateView.as_view(), name='rate_create'),

]