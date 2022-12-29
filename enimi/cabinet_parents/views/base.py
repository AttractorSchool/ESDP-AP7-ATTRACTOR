from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
from django.views.generic import DetailView, CreateView, UpdateView, ListView
from django.http import HttpResponse
from django.core import serializers
import base64

from accounts.forms import AccountForm, ChildrenForm
from accounts.forms.accounts import AvatarForm
from accounts.models import Account
from django.http.response import JsonResponse

from cabinet_parents.forms import SurveyForm

from cabinet_parents.models import Survey


class ParentProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'parent_detail.html'
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        children = Account.objects.filter(is_deleted=False, parent=self.request.user)
        context['children'] = children
        context['student_register_form'] = AccountForm()
        context['student_without_email_register_form'] = ChildrenForm()
        context['main_form'] = SurveyForm()
        return context


class ParentCreateChildrenView(CreateView):
    template_name = 'account_register.html'
    model = Account
    form_class = AccountForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        user = request.user
        answer = {}

        if form.is_valid():
            account = form.save(commit=False)
            account.username = account.email
            account.type = 'student'
            account.parent = user
            account.save()
            # children = Account.objects.filter(is_deleted=False, parent=request.user)
            return redirect('parents_cabinet_detail', pk=user.pk)
        context = {}
        context['form'] = form
        return self.render_to_response(context)


class ParentCreateChildrenWithoutEmailView(CreateView):
    template_name = 'account_without_email_register.html'
    model = Account
    form_class = ChildrenForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        user = request.user
        if form.is_valid():
            child = form.save(commit=False)
            child.email = user.email.split("@")[0] + child.first_name + '@' + user.email.split("@")[1]
            child.username = child.email
            child.parent = Account.objects.get(pk=kwargs['pk'])
            child.with_email = False
            child.save()
            return redirect('parents_cabinet_detail', pk=child.parent.pk)
        context = {}
        context['form'] = form
        return self.render_to_response(context)


class ParentChildrenSurveysView(LoginRequiredMixin, ListView):
    template_name = 'parent_children_detail_surveys.html'
    model = Account
    context_object_name = 'vacancies'

    def get_context_data(self, *, object_list=None, **kwargs):
        parent = Account.objects.get(id=self.kwargs['pk'])
        children = Account.objects.filter(is_deleted=False, parent=parent)
        context = super(ParentChildrenSurveysView, self).get_context_data(object_list=object_list, **kwargs)
        context['children'] = children
        context['student_register_form'] = AccountForm()
        context['student_without_email_register_form'] = ChildrenForm()
        context['main_form'] = SurveyForm()
        return context


class CreateParentChildrenSurveyView(LoginRequiredMixin, CreateView):
    template_name = 'create_survey_student.html'
    form_class = SurveyForm
    model = Survey

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user_id = self.kwargs['pk']
            survey = form.save()
            student = Account.objects.get(id=self.kwargs['pk'])
            print(student)
            student.with_survey = True
            student.save()
            return redirect('parent_children_surveys', student.parent.pk)
        context = {}
        context['form'] = form
        return self.render_to_response(context)


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CreateParentChildrenSurveyView, self).get_context_data(object_list=object_list, **kwargs)
        student = Account.objects.get(id=self.kwargs['pk'])
        context['student'] = student
        return context

    def get_success_url(self):
        return redirect('parent_children_surveys', self.kwargs['pk'])


class UpdateParentChildrenSurveyView(UpdateView):
    template_name = 'main_survey_edit.html'
    form_class = SurveyForm
    model = Survey
    context_object_name = 'survey'

    def get_context_data(self, **kwargs):
        context = super(UpdateParentChildrenSurveyView, self).get_context_data(**kwargs)
        context['form'] = SurveyForm(instance=self.object)
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        child = Account.objects.get(id=self.object.user_id)
        print(child)
        return redirect('parent_children_surveys', pk=child.parent.pk)



# class GetDataForSurveysView(CreateView):
#     model = Account
#
#     def get(self, request, *args, **kwargs):
#         answer = {}
#         children = Account.objects.filter(is_deleted=False, parent=request.user)
#
#         answer = serializers.serialize('json', children)
#         return HttpResponse(answer, content_type='application/json')
#

# def upload_file(request, pk):
#     file = request.FILES.get("avatar")
#     fss = FileSystemStorage()
#     url = str(file)
#     filename = fss.save(file.name, file)
#     # url = fss.url(filename)
#     account = Account.objects.get(id=pk)
#     account.avatar = url
#     account.save()
#     return JsonResponse({"link": ('/uploads/' + url), "pk": pk})
#

