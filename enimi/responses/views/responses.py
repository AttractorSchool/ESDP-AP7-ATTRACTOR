from django.contrib.auth.mixins import LoginRequiredMixin
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
        students_response = Response.objects.filter(author_id=survey.user.pk).filter(cabinet_tutor_id=self.request.user.tutor.pk)
        if students_response:
            response = Response.objects.get(id=students_response[0].pk)
            context['response'] = response
            context['response_form'] = ResponseForm
        else:
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
            in_table = Response.objects.filter(survey_id=survey.pk, author_id=request.user.pk)
            if not in_table:
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
            else:
                context['response_form'] = form
                context['error'] = 'Ранее вы уже делали отклик на этого пользователя'
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
        tutors_response = Response.objects.filter(author_id=cabinet_tutor.user.pk,
                                                  survey_id=self.request.user.survey.pk)
        if tutors_response:
            response = Response.objects.get(id=tutors_response[0].pk)
            context['response'] = response
            context['response_form'] = ResponseForm
        else:
            subjects = Subject.objects.all()
            context['subjects'] = subjects
            context['response_form'] = ResponseForm
            # (current_survey=survey)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        context = {}
        if form.is_valid():
            tutor_cabinet = TutorCabinets.objects.get(id=self.kwargs['pk'])
            in_table = Response.objects.filter(cabinet_tutor_id=tutor_cabinet.pk, author_id=request.user.pk)
            if not in_table:
                form.instance.author_id = self.request.user.pk
                form.instance.cabinet_tutor_id = self.kwargs['pk']
                response = form.save()
                response_from_student_to_tutor(response, tutor_cabinet.user)
                response_from_student_to_self(response, tutor_cabinet.user)
                context['response_form'] = form
                context['ok'] = 'Отклик успешно добавлен'
                return self.render_to_response(context)
            else:
                context['response_form'] = form
                context['error'] = 'Ранее вы уже делали отклик на этого пользователя'
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
            cabinet_tutor = TutorCabinets.objects.get(id=kwargs['pk'])
            child = survey.user
            tutors_response = Response.objects.filter(author_id=cabinet_tutor.user.pk,
                                                      survey_id=child.survey.pk)
            if tutors_response:
                print('AAAAAAA')
                response = Response.objects.get(id=tutors_response[0].pk)
                context['response'] = response
                context['response_form'] = ResponseForm
                return self.render_to_response(context)
            in_table = Response.objects.filter(author_id=child.pk, cabinet_tutor_id=self.kwargs['pk'])
            if not in_table:
                form.instance.author_id = child.pk
                form.instance.cabinet_tutor_id = self.kwargs['pk']
                response = form.save()
                context['response_form'] = form
                context['ok'] = 'Отклик успешно добавлен'
                tutor = get_object_or_404(TutorCabinets, pk=self.kwargs['pk']).user
                response_to_parent_from_self(response, child, tutor)
                response_from_student_to_tutor(response, tutor)
                return self.render_to_response(context)
            else:
                context['response_form'] = form
                context['error'] = 'Ранее вы уже делали отклик на этого пользователя'
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
