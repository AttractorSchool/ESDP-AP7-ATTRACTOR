from django.urls import path

from board_tutors_students.views.base import BoardTutorView, BoardStudentView

urlpatterns = [
    path('board_tutor', BoardTutorView.as_view(), name='board_tutor'),
    path('board_student', BoardStudentView.as_view(), name='board_student'),
]
