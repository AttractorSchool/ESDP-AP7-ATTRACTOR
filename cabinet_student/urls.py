from django.urls import path

from cabinet_student.views.base import *

urlpatterns = [
    path('<int:pk>/', StudentProfileView.as_view(), name='student_cabinet_detail'),
    path('<int:pk>/student/create_survey', CreateStudentSurveyView.as_view(), name='student_create_survey'),
    path('<int:pk>/student/detail_survey', StudentDetailSurveyView.as_view(), name='student_detail_survey'),
    path('<int:pk>/student/update_survey', UpdateStudentSurveyView.as_view(), name='main_survey_update'),
    path('<int:pk>/student/offline_study_tutor_area_survey_update',
         UpdateStudentOfflineStudyTutorAreaView.as_view(), name='offline_study_tutor_area_survey_update'),
    path('<int:pk>/student/offline_study_student_area_survey_update',
         UpdateStudentOfflineStudyStudentAreaView.as_view(),
         name='offline_study_student_area_survey_update'),
    path('<int:pk>/student/offline_study_tutor_area_reset',
         ResetStudentOfflineStudyTutorAreaView.as_view(), name='reset_tutor_area_for_student'),
    path('<int:pk>/student/offline_study_student_area_reset',
         ResetStudentOfflineStudyStudentAreaView.as_view(), name='reset_student_area_for_student'),
    path('<int:pk>/to_me_student_responses', StudentToMeResponsesView.as_view(), name='to_me_student_responses'),
    path('<int:pk>/student_on_tutor_responses', StudentOnTutorResponsesView.as_view(),
         name='student_on_tutor_responses'),

    path('my_tutors/<int:pk>/', MyTutorsView.as_view(), name='my_tutors'),
    path('my_reviews/<int:pk>/', ReviewListView.as_view(), name='my_reviews'),

    path('review_page/<int:pk>/', ReviewMakeView.as_view(), name='review_page'),
    path('make_review/<int:pk>/', ReviewCreateView.as_view(), name='make_review'),
    path('<int:pk>/student_rates/', StudentRatesView.as_view(), name='student_rates')
]
