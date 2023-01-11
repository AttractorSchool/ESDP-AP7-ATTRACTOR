from django.urls import path

from board_tutors_students.views.base import BoardTutorView

urlpatterns = [
    path('', BoardTutorView.as_view(), name='board_tutor'),
]

