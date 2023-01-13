from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import CreateView

from cabinet_tutors.models import TutorCabinets
from responses.models.responses import Response
from responses.forms import ResponseForm
from cabinet_parents.models import Survey, Subject


class StudentAddResponseView(LoginRequiredMixin, CreateView):
    template_name = 'to_student_response_create.html'
    model = Response
    form_class = ResponseForm

    def get_context_data(self, **kwargs):
        print(self.kwargs['pk'])
        context = super(StudentAddResponseView, self).get_context_data(**kwargs)
        survey = Survey.objects.get(id=self.kwargs['pk'])
        print(survey)
        subjects = Subject.objects.all()
        context['subjects'] = subjects
        context['response_form'] = ResponseForm
        # (current_survey=survey)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.instance.author_id = self.request.user.pk
            form.instance.survey_id = self.kwargs['pk']
            form.save()
            return redirect('board_student')
        context = {}
        context['response_form'] = form
        return self.render_to_response(context)


class TutorAddResponseView(LoginRequiredMixin, CreateView):
    template_name = 'to_tutor_response_create.html'
    model = Response
    form_class = ResponseForm

    def get_context_data(self, **kwargs):
        print(self.kwargs['pk'])
        context = super(TutorAddResponseView, self).get_context_data(**kwargs)
        cabinet_tutor = TutorCabinets.objects.get(id=self.kwargs['pk'])
        print(cabinet_tutor)
        subjects = Subject.objects.all()
        context['subjects'] = subjects
        context['response_form'] = ResponseForm
        # (current_survey=survey)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.instance.author_id = self.request.user.pk
            form.instance.cabinet_tutor_id = self.kwargs['pk']
            form.save()
            return redirect('board_student')
        context = {}
        context['response_form'] = form
        return self.render_to_response(context)
