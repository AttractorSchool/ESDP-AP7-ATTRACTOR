from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, CreateView, UpdateView, ListView
from django.http import HttpResponse
from django.core import serializers
import base64

from accounts.forms import AccountForm, ChildrenForm
from accounts.forms.accounts import AvatarForm
from accounts.models import Account
from django.http.response import JsonResponse

from cabinet_student.forms import SurveyForm, StudentAreaForm, TutorAreaForm

from cabinet_parents.models import Survey, TutorArea, Region, City, District, StudentArea


class StudentProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'student_detail.html'
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_register_form'] = AccountForm()
        context['main_form'] = SurveyForm()
        return context



class CreateStudentSurveyView(LoginRequiredMixin, CreateView):
    template_name = 'create_survey_student.html'
    form_class = SurveyForm
    model = Survey

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.instance.user_id = self.kwargs['pk']
            form.save()
            student = Account.objects.get(id=self.kwargs['pk'])
            survey = student.survey

            if request.POST['tutor_region']:
                tutor_region = Region.objects.get(id=request.POST['tutor_region'])
            else:
                tutor_region = Region.objects.get(region='Не указано')
            if request.POST['tutor_city']:
                tutor_city = City.objects.get(id=request.POST['tutor_city'])
            else:
                tutor_city = City.objects.get(city='Не указано')
            if request.POST['tutor_district']:
                tutor_district = District.objects.get(id=request.POST['tutor_district'])
            else:
                tutor_district = District.objects.get(district='Не указано')
            tutor_area = TutorArea.objects.create(tutor_region=tutor_region, tutor_city=tutor_city,
                                                  tutor_district=tutor_district)

            survey.tutor_area = tutor_area
            survey.save()

            if request.POST['student_region']:
                student_region = Region.objects.get(id=request.POST['student_region'])
            else:
                student_region = Region.objects.get(region='Не указано')
            if request.POST['student_city']:
                student_city = City.objects.get(id=request.POST['student_city'])
            else:
                student_city = City.objects.get(city='Не указано')
            if request.POST['student_district']:
                student_district = District.objects.get(id=request.POST['student_district'])
            else:
                student_district = District.objects.get(district='Не указано')
            student_area = StudentArea.objects.create(student_region=student_region, student_city=student_city,
                                                      student_district=student_district)
            survey.student_area = student_area
            survey.save()
            student.with_survey = True
            student.save()
            return redirect('student_cabinet_detail', student.pk)
        context = {}
        context['form'] = form
        return self.render_to_response(context)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CreateStudentSurveyView, self).get_context_data(object_list=object_list, **kwargs)
        student = Account.objects.get(id=self.kwargs['pk'])
        context['student'] = student
        context['tutor_adr'] = TutorAreaForm()
        context['student_adr'] = StudentAreaForm()
        return context

    def get_success_url(self):
        return redirect('student_cabinet_detail', self.kwargs['pk'])


class StudentDetailSurveyView(LoginRequiredMixin, ListView):
    template_name = 'student_detail_survey.html'
    model = Account


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(StudentDetailSurveyView, self).get_context_data(object_list=object_list, **kwargs)
        context['main_form'] = SurveyForm()
        return context


class UpdateStudentSurveyView(UpdateView):
    template_name = 'main_survey_update.html'
    form_class = SurveyForm
    model = Survey
    context_object_name = 'survey'

    def get_context_data(self, **kwargs):
        context = super(UpdateStudentSurveyView, self).get_context_data(**kwargs)
        context['form'] = SurveyForm(instance=self.object)
        return context

    def get_success_url(self):
        survey = self.object
        student = Account.objects.get(id=survey.user_id)
        return reverse('student_detail_survey', kwargs={'pk': student.pk})


class UpdateStudentOfflineStudyTutorAreaView(UpdateView):
    template_name = 'offline_study_tutor_area_update.html'
    form_class = TutorAreaForm
    model = TutorArea
    context_object_name = 'tutor_area'

    def get_context_data(self, **kwargs):
        context = super(UpdateStudentOfflineStudyTutorAreaView, self).get_context_data(**kwargs)
        context['form'] = TutorAreaForm(instance=self.object)
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        survey = Survey.objects.get(tutor_area_id=self.object.pk)
        student = Account.objects.get(id=survey.user_id)
        return redirect('student_detail_survey', pk=student.pk)


class UpdateStudentOfflineStudyStudentAreaView(UpdateView):
    template_name = 'offline_study_student_area_update.html'
    form_class = StudentAreaForm
    model = StudentArea
    context_object_name = 'student_area'

    def get_context_data(self, **kwargs):
        context = super(UpdateStudentOfflineStudyStudentAreaView, self).get_context_data(**kwargs)
        context['form'] = StudentAreaForm(instance=self.object)
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        survey = Survey.objects.get(student_area_id=self.object.pk)
        student = Account.objects.get(id=survey.user_id)
        return redirect('student_detail_survey', pk=student.pk)


class ResetStudentOfflineStudyTutorAreaView(UpdateView):
    model = TutorArea
    context_object_name = 'tutor_area'

    def post(self, request, **kwargs):
        tutor_area = TutorArea.objects.get(id=kwargs['pk'])

        tutor_area.tutor_region = Region.objects.get(region='Не указано')
        tutor_area.tutor_city = City.objects.get(city='Не указано')
        tutor_area.tutor_district = District.objects.get(district='Не указано')

        tutor_area.save()
        survey = Survey.objects.get(tutor_area_id=tutor_area.pk)
        student = Account.objects.get(id=survey.user_id)
        return redirect('student_detail_survey', pk=student.pk)


class ResetStudentOfflineStudyStudentAreaView(UpdateView):
    model = StudentArea
    context_object_name = 'student_area'

    def post(self, request, **kwargs):
        student_area = StudentArea.objects.get(id=kwargs['pk'])

        student_area.student_region = Region.objects.get(region='Не указано')
        student_area.student_city = City.objects.get(city='Не указано')
        student_area.student_district = District.objects.get(district='Не указано')

        student_area.save()
        survey = Survey.objects.get(student_area_id=student_area.pk)
        student = Account.objects.get(id=survey.user_id)
        return redirect('student_detail_survey', pk=student.pk)


