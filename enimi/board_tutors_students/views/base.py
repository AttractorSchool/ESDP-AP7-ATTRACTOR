from django.views.generic import ListView, DetailView, TemplateView

from cabinet_parents.models import Survey
from cabinet_tutors.models import TutorCabinets


class BoardTutorView(ListView):
    template_name = 'board_tutor.html'
    model = TutorCabinets
    context_object_name = 'tutors'


class BoardStudentView(ListView):
    template_name = 'board_student.html'
    model = Survey
    context_object_name = 'surveys'
