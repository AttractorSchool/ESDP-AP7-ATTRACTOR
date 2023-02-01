from django.urls import path

from board_tutors_students.views.base import BoardTutorView, BoardStudentView, TutorBoardDetailPageView

urlpatterns = [
    path('board_tutor', BoardTutorView.as_view(), name='board_tutor'),
    path('board_tutor/<int:pk>/detail', TutorBoardDetailPageView.as_view(), name='tutor_board_detail_page'),
    path('board_student', BoardStudentView.as_view(), name='board_student'),
]
