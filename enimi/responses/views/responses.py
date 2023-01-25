from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView

from cabinet_tutors.models import TutorCabinets
from notifications.messages import response_to_parent_from_self, response_from_student_to_tutor, \
    response_from_tutor_to_self, response_from_tutor_to_student, response_from_student_to_self, \
    response_from_tutor_to_student_with_parent
from notifications.models import Notifications
from responses.models.responses import Response
from responses.forms import ResponseForm, ParentResponseForm
from cabinet_parents.models import Survey, Subject
from accounts.models import Account


# FromTutorToStudent
class StudentAddResponseView(LoginRequiredMixin, CreateView):
    template_name = 'to_student_response_create.html'
    model = Response
    form_class = ResponseForm

    def get_context_data(self, **kwargs):
        context = super(StudentAddResponseView, self).get_context_data(**kwargs)
        survey = Survey.objects.get(id=self.kwargs['pk'])
        subjects = Subject.objects.all()
        context['subjects'] = subjects
        context['response_form'] = ResponseForm
        # (current_survey=survey)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        context = {}
        if form.is_valid():
            survey = Survey.objects.get(id=self.kwargs['pk'])
            response_exists = Q(survey=survey, author=request.user) | Q(author=survey.user,
                                                                        cabinet_tutor=request.user.tutor)
            response_already_exists = Response.objects.filter(response_exists)
            if response_already_exists:
                context['response_form'] = form
                context['error'] = 'Отклик с данным пользователем уже существует'
                context['response_pk'] = response_already_exists.first().pk
                return self.render_to_response(context)
            else:
                form.instance.author_id = self.request.user.pk
                form.instance.survey_id = self.kwargs['pk']
                response = form.save()
                context['response_form'] = form
                context['ok'] = 'Отклик успешно добавлен'
                if survey.user.with_email:
                    response_from_tutor_to_student(response, survey.user)
                else:
                    response_from_tutor_to_student_with_parent(response, survey.user)
                response_from_tutor_to_self(response, survey.user)
                return self.render_to_response(context)
        context['response_form'] = form
        return self.render_to_response(context)


# FromStudentToTutor
class TutorAddResponseView(LoginRequiredMixin, CreateView):
    template_name = 'to_tutor_response_create.html'
    model = Response
    form_class = ResponseForm

    def get_context_data(self, **kwargs):
        context = super(TutorAddResponseView, self).get_context_data(**kwargs)
        cabinet_tutor = TutorCabinets.objects.get(id=self.kwargs['pk'])
        subjects = Subject.objects.all()
        context['subjects'] = subjects
        context['response_form'] = ResponseForm
        # (current_survey=survey)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        context = {}
        if form.is_valid():
            cabinet_tutor = TutorCabinets.objects.get(id=self.kwargs['pk'])
            response_exists = Q(author=cabinet_tutor.user, survey=request.user.survey) | Q(author=request.user,
                                                                                           cabinet_tutor=cabinet_tutor)
            response_already_exists = Response.objects.filter(response_exists)
            if response_already_exists:
                context['response_form'] = form
                context['error'] = 'Отклик с данным пользователем уже существует'
                context['response_pk'] = response_already_exists.first().pk
                return self.render_to_response(context)
            else:
                form.instance.author_id = self.request.user.pk
                form.instance.cabinet_tutor_id = self.kwargs['pk']
                response = form.save()
                response_from_student_to_tutor(response, cabinet_tutor.user)
                response_from_student_to_self(response, cabinet_tutor.user)
                context['response_form'] = form
                context['ok'] = 'Отклик успешно добавлен'
                return self.render_to_response(context)
        context['response_form'] = form
        return self.render_to_response(context)


# FromParentToTutor
class ParentAddResponseView(LoginRequiredMixin, CreateView):
    template_name = 'parent_on_tutor_response_create.html'
    model = Response
    form_class = ResponseForm

    def get_context_data(self, **kwargs):
        context = super(ParentAddResponseView, self).get_context_data(**kwargs)
        cabinet_tutor = TutorCabinets.objects.get(id=self.kwargs['pk'])
        subjects = Subject.objects.all()
        parent = self.request.user
        children = Account.objects.filter(parent_id=parent.pk).values('id', 'survey')
        survey_id_list = []
        for child in children:
            survey_pk = child.get('survey')
            survey_id_list.append(survey_pk)
        surveys = Survey.objects.filter(id__in=survey_id_list)
        context['subjects'] = subjects
        context['response_form'] = ParentResponseForm(survey_id_list=survey_id_list)
        # (current_survey=survey)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        context = {}
        if form.is_valid():
            survey = Survey.objects.get(id=request.POST['survey'])
            child = survey.user
            tutor_cabinet = get_object_or_404(TutorCabinets, pk=self.kwargs['pk'])
            response_exists = Q(author=child, cabinet_tutor=tutor_cabinet) | Q(author=tutor_cabinet.user, survey=survey)
            response_already_exists = Response.objects.filter(response_exists)
            if response_already_exists:
                context['response_form'] = form
                context['error'] = 'Отклик с данным пользователем уже существует'
                context['response_pk'] = response_already_exists.first().pk
                return self.render_to_response(context)
            else:
                form.instance.author_id = child.pk
                form.instance.cabinet_tutor_id = self.kwargs['pk']
                response = form.save()
                context['response_form'] = form
                context['ok'] = 'Отклик успешно добавлен'
                response_to_parent_from_self(response, child, tutor_cabinet.user)
                response_from_student_to_tutor(response, tutor_cabinet.user)
                return self.render_to_response(context)

        context['response_form'] = form
        return self.render_to_response(context)

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST, request.FILES)
    #     print(request.POST)
    #     if form.is_valid():
    #         survey = Survey.objects.get(id=request.POST['survey'])
    #         child = survey.user
    #         form.instance.author_id = child.pk
    #         # form.instance.survey_id = request.POST['survey']
    #         form.instance.cabinet_tutor_id = self.kwargs['pk']
    #         form.save()
    #         return redirect('board_tutor')
    #     context = {}
    #     context['response_form'] = form
    #     return self.render_to_response(context)
