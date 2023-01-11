from django.urls import path

from cabinet_tutors.views.education import EducationCreateView, EducationDeleteView
from cabinet_tutors.views.subjects_and_costs import SubjectsAndCostCreateView, SubjectsAndCostDeleteView
from cabinet_tutors.views.tutor_cabinets import TutorCabinetView, TutorCabinetUpdateView

urlpatterns = [
    path('<int:pk>/', TutorCabinetView.as_view(), name='tutor_cabinet'),
    path('<int:pk>/main/update', TutorCabinetUpdateView.as_view(), name='tutor_main_update'),

    path('<int:tpk>/education/create/', EducationCreateView.as_view(), name='education_create_or_update'),
    path('<int:tpk>/education/<int:pk>/delete/', EducationDeleteView.as_view(), name='education_delete'),

    path('<int:tpk>/subjects-and-costs/create-or-update/', SubjectsAndCostCreateView.as_view(),
         name='subjects_and_costs_create_or_update'),
    path('<int:tpk>/subjects-and-costs/<int:pk>/delete/', SubjectsAndCostDeleteView.as_view(),
         name='subjects_and_costs_delete'),
]
