from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import UpdateView, CreateView, DeleteView

from cabinet_tutors.forms.education import EducationForm
from cabinet_tutors.models import Education


class EducationCreateView(CreateView):
    template_name = 'education/education_create.html'
    form_class = EducationForm
    model = Education

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            education = form.save(commit=False)
            education.save()
            request.user.tutor.education.add(education)
            return redirect('tutor_cabinet', pk=education.tutors.first().pk)
        context = {}
        context['form'] = form
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse('tutor_cabinet', kwargs={'pk': self.request.user.tutor.pk})


# Create your views here.
class EducationUpdateView(UpdateView):
    template_name = 'education/education_update.html'
    model = Education
    form_class = EducationForm
    context_object_name = 'education'

    def get_success_url(self):
        return reverse('tutor_cabinet', kwargs={'pk': self.object.tutors.first().pk})


class EducationDeleteView(DeleteView):
    template_name = 'education/education_delete.html'
    model = Education
    context_object_name = 'education'

    def get_success_url(self):
        return reverse('tutor_cabinet', kwargs={'pk': self.request.user.tutor.pk})
