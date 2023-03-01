from django.urls import reverse
from django.views.generic import DetailView, UpdateView
from cabinet_tutors.forms.tutor_cabinets import TutorCabinetForm
from cabinet_tutors.models import TutorCabinets, Education, SubjectsAndCosts, TutorStudyFormats
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class TutorCabinetView(LoginRequiredMixin,DetailView):
    template_name = 'tutor_cabinet.html'
    model = TutorCabinets
    context_object_name = 'tutor'

    def get(self, request, *args, **kwargs):
        self.extra_context = {
            'educations': Education.objects.filter(tutors=kwargs.get('pk')).order_by('created_at'),
            'subjects_and_costs': SubjectsAndCosts.objects.filter(tutors=kwargs.get('pk')),
            'study_formats': TutorStudyFormats.objects.filter(tutors=kwargs.get('pk')),
            'tutor_cabinet': '1'
        }
        return super(TutorCabinetView, self).get(request, *args, **kwargs)


class TutorCabinetUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'tutor_about_update.html'
    model = TutorCabinets
    form_class = TutorCabinetForm

    def get_success_url(self):
        return reverse('tutor_cabinet', kwargs={'pk': self.object.pk})

