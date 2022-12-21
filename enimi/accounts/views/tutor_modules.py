from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView

from accounts.forms.tutor_modules import TutorModuleForm
from accounts.models import TutorModule


class TutorModuleCreateView(CreateView):
    template_name = 'tutor_module_creation.html'
    model = TutorModule
    form_class = TutorModuleForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            tutor = form.save(commit=False)
            tutor.user = request.user
            tutor.save()
            return redirect('index')
        context = {}
        context['form'] = form
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse('index')
