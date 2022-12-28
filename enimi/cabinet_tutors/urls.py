from django.urls import path

from cabinet_tutors.views.education import EducationUpdateView, EducationCreateView, EducationDeleteView
from cabinet_tutors.views.tutor_modules import TutorCabinetView, TutorCabinetUpdateView

urlpatterns = [
    path('<int:pk>/', TutorCabinetView.as_view(), name='tutor_cabinet'),
    path('<int:pk>/main/update', TutorCabinetUpdateView.as_view(), name='tutor_main_update'),

    path('<int:tpk>/education/create/', EducationCreateView.as_view(), name='education_create'),
    path('<int:tpk>/education/<int:pk>/update/', EducationUpdateView.as_view(), name='education_update'),
    path('<int:tpk>/education/<int:pk>/delete/', EducationDeleteView.as_view(), name='education_delete'),
]
