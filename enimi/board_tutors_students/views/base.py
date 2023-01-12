from django.views.generic import ListView, DetailView, TemplateView

from cabinet_tutors.models import TutorCabinets


class BoardTutorView(ListView):
    template_name = 'board_tutor.html'
    model = TutorCabinets

    context_object_name = 'tutors'
