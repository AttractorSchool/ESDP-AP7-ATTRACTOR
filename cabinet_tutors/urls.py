from django.urls import path

from cabinet_tutors.views.education import EducationCreateUpdateView, EducationDeleteView
from cabinet_tutors.views.main_page_schedule import MainPageScheduleView
from cabinet_tutors.views.students_of_tutor import ToMyStudentAddView, MyStudentsView
from cabinet_tutors.views.study_formats import TutorStudyFormatsUpdateView, TutorStudyFormatsCreateView, \
    TutorStudyFormatsDeleteView, SecondTutorStudyFormatsCreateView
from cabinet_tutors.views.subjects_and_costs import SubjectsAndCostCreateUpdateView, SubjectsAndCostDeleteView
from cabinet_tutors.views.tutor_cabinets import TutorCabinetView, TutorCabinetUpdateView
from cabinet_tutors.views.responses import OnStudentsFromTutorView, OnTutorFromStudentResponsesView
from cabinet_tutors.views.reviews import OnMeReviewsView

urlpatterns = [
    path('<int:pk>/', TutorCabinetView.as_view(), name='tutor_cabinet'),
    path('<int:pk>/main/update', TutorCabinetUpdateView.as_view(), name='tutor_main_update'),

    path('<int:tpk>/education/create/', EducationCreateUpdateView.as_view(), name='education_create_or_update'),
    path('<int:tpk>/education/<int:pk>/delete/', EducationDeleteView.as_view(), name='education_delete'),

    path('<int:tpk>/subjects-and-costs/create-or-update/', SubjectsAndCostCreateUpdateView.as_view(),
         name='subjects_and_costs_create_or_update'),
    path('<int:tpk>/subjects-and-costs/<int:pk>/delete/', SubjectsAndCostDeleteView.as_view(),
         name='subjects_and_costs_delete'),

    path('<int:tpk>/study-formats/create/', TutorStudyFormatsCreateView.as_view(), name='tutor_study_formats_create'),
    path('<int:tpk>/study-formats/<int:pk>/update/', TutorStudyFormatsUpdateView.as_view(),
         name='tutor_study_formats_update'),
    path('<int:tpk>/study-formats/<int:pk>/delete/', TutorStudyFormatsDeleteView.as_view(),
         name='tutor_study_formats_delete'),
    path('<int:pk>/tutor-responses-on-students/', OnStudentsFromTutorView.as_view(), name='my_responses_on_students'),
    path('<int:pk>/students-responses-on-tutor/', OnTutorFromStudentResponsesView.as_view(),
         name='students_on_tutor_responses'),
    path('add_user_to_my_students/<int:pk>/', ToMyStudentAddView.as_view(),
             name='add_user_to_my_students'),
    path('<int:pk>/my_students/', MyStudentsView.as_view(),
                 name='my_students'),
    path('<int:pk>/reviews/', OnMeReviewsView.as_view(),
                     name='on_tutor_reviews'),
    path("main_tab_schedule/", MainPageScheduleView.as_view(), name="main_tab_schedule"),
]
