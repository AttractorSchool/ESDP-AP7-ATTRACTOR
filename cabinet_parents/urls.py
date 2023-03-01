from django.urls import path

from cabinet_parents.views.base import ParentProfileView, ParentCreateChildrenView, \
    ParentCreateChildrenWithoutEmailView, ParentChildrenSurveysView, CreateParentChildrenSurveyView, \
    UpdateParentChildrenSurveyView, UpdateParentChildrenOfflineStudyTutorAreaSurveyView, \
    UpdateParentChildrenOfflineStudyStudentAreaSurveyView, ResetParentChildrenOfflineStudyTutorAreaSurveyView,\
    ResetParentChildrenOfflineStudyStudentAreaSurveyView, ToMyChildrenResponsesView, FromParentOnTutorResponsesView, \
    TutorsOfMyChildrenView, FromParentReviewMakeView, FromParentReviewCreateView, FromParentReviewsView, ParentChildrenRatesView

urlpatterns = [
    path('<int:pk>/', ParentProfileView.as_view(), name='parents_cabinet_detail'),
    path('<int:pk>/create/children/', ParentCreateChildrenView.as_view(), name='parent_create_children'),
    path('<int:pk>/create/children_without_email/', ParentCreateChildrenWithoutEmailView.as_view(), name='parent_create_children_without_email'),
    path('<int:pk>/parent_children_surveys', ParentChildrenSurveysView.as_view(), name='parent_children_surveys'),
    path('<int:pk>/parent_children_surveys/create_survey', CreateParentChildrenSurveyView.as_view(), name='parent_children_create_surveys'),
    path('<int:pk>/parent_children_surveys/update_survey', UpdateParentChildrenSurveyView.as_view(), name='main_child_survey_update'),
    path('<int:pk>/parent_children_surveys/offline_study_tutor_area_survey_update',
         UpdateParentChildrenOfflineStudyTutorAreaSurveyView.as_view(), name='offline_child_study_tutor_area_survey_update'),
    path('<int:pk>/parent_children_surveys/offline_study_student_area_survey_update',
         UpdateParentChildrenOfflineStudyStudentAreaSurveyView.as_view(), name='offline_cheild_study_student_area_survey_update'),
    path('<int:pk>/parent_children_surveys/offline_study_tutor_area_reset',
         ResetParentChildrenOfflineStudyTutorAreaSurveyView.as_view(), name='reset_child_tutor_area_for_student'),
    path('<int:pk>/parent_children_surveys/offline_study_student_area_reset',
         ResetParentChildrenOfflineStudyStudentAreaSurveyView.as_view(), name='reset_child_student_area_for_student'),
    path('<int:pk>/to_my_children_responses', ToMyChildrenResponsesView.as_view(), name='to_my_children_responses'),
    path('<int:pk>/from_me-parent_on_tutor_responses', FromParentOnTutorResponsesView.as_view(),
             name='from_me-parent_on_tutor_responses'),
    path('<int:pk>/my_children_tutors', TutorsOfMyChildrenView.as_view(), name='my_children_tutors'),

    path('<int:pk>/review_page/', FromParentReviewMakeView.as_view(), name='make_review_from_parent'),
    path('<int:pk>/make_review/', FromParentReviewCreateView.as_view(), name='parent_make_review'),
    path('<int:pk>/from_parent_on_tutor_reviews/', FromParentReviewsView.as_view(), name='from_parent_on_tutor_reviews'),
    path('<int:pk>/student_rates/', ParentChildrenRatesView.as_view(), name='parent_children_rates')
    # path('<int:pk>/get_children_surveys/', GetDataForSurveysView.as_view(), name='get_children_surveys'),
    # path('<int:pk>/change_avatar/', upload_file, name='change_avatar'),
]

