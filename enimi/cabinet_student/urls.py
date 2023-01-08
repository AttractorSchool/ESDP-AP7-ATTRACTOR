from django.urls import path

from cabinet_student.views.base import StudentProfileView, CreateStudentSurveyView, UpdateStudentSurveyView, StudentDetailSurveyView, \
                                         UpdateStudentOfflineStudyTutorAreaView,\
                                        UpdateStudentOfflineStudyStudentAreaView, ResetStudentOfflineStudyTutorAreaView, \
                                        ResetStudentOfflineStudyStudentAreaView


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
]
