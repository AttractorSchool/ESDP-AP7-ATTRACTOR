from django.urls import reverse
from django.views.generic import UpdateView, CreateView, DeleteView

from cabinet_tutors.forms.education import EducationForm, EducationFormSet
from cabinet_tutors.models import Education


class EducationCreateUpdateView(CreateView):
    template_name = 'education/education_create_or_update.html'
    form_class = EducationForm
    model = Education

    def get_context_data(self, **kwargs):
        context = super(EducationCreateUpdateView, self).get_context_data(**kwargs)
        context['formset'] = EducationFormSet(
            queryset=Education.objects.filter(tutors=self.request.user.tutor).order_by('id'))
        return context

    def post(self, request, *args, **kwargs):
        formset = EducationFormSet(request.POST)
        if formset.is_valid():
            return self.form_valid(formset)

    def form_valid(self, formset):
        educations = formset.save(commit=False)
        for education in educations:
            education.save()
            self.request.user.tutor.education.add(education)
        return super().form_valid(formset)

    def get_success_url(self):
        return reverse('tutor_cabinet', kwargs={'pk': self.request.user.tutor.pk})


class EducationDeleteView(DeleteView):
    model = Education
    context_object_name = 'education'

    def get_success_url(self):
        return reverse('tutor_cabinet', kwargs={'pk': self.request.user.tutor.pk})
