from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from accounts.models import Account
from cabinet_tutors.models import TutorCabinets
from responses.models import Response


class OnStudentsFromTutorView(LoginRequiredMixin, ListView):
    template_name = 'my_responses_on_student.html'
    model = Response

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(OnStudentsFromTutorView, self).get_context_data(object_list=object_list, **kwargs)
        tutor_cabinet = TutorCabinets.objects.get(id=self.kwargs['pk'])
        responses = Response.objects.filter(author_id=tutor_cabinet.user.pk)
        context['responses'] = responses
        context['chat_page_1'] = '1'
        return context


class OnTutorFromStudentResponsesView(LoginRequiredMixin, ListView):
    template_name = 'on_me_from_student_responses.html'
    model = Response

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(OnTutorFromStudentResponsesView, self).get_context_data(object_list=object_list, **kwargs)
        user = Account.objects.get(id=self.kwargs['pk'])
        responses = Response.objects.filter(cabinet_tutor_id=user.tutor.pk)
        context['responses'] = responses
        context['chat_page_2'] = '1'
        return context
