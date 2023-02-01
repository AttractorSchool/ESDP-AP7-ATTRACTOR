from django.urls import path

from board_tutors_students.views.base import BoardTutorView, BoardStudentView, TutorBoardDetailPageView, \
    StudentBoardDetailPageView

urlpatterns = [
    path('board_tutor', BoardTutorView.as_view(), name='board_tutor'),
    path('board_tutor/<int:pk>/detail', TutorBoardDetailPageView.as_view(), name='tutor_board_detail_page'),
    path('board_student', BoardStudentView.as_view(), name='board_student'),
    path('board_student/<int:pk>/detail', StudentBoardDetailPageView.as_view(), name='student_board_detail_page'),
]
