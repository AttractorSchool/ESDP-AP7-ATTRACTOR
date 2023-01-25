from django.http import HttpResponse, JsonResponse
from django.views.generic import CreateView, ListView

from accounts.models import Account
from cabinet_tutors.models import MyStudent, TutorCabinets
from notifications.messages import student_added_message_to_tutor, student_added_message_to_student, \
    student_added_message_to_parent


class ToMyStudentAddView(CreateView):
    model = Account

    def get(self, request, *args, **kwargs):
        error = {}
        tutor = request.user
        student = Account.objects.get(id=kwargs['pk'])
        in_table = MyStudent.objects.filter(student=student, tutor=tutor)
        if not in_table:
            my_student = MyStudent.objects.create(tutor=tutor, student=student)
            student_added_message_to_tutor(tutor, student)
            if student.parent and student.with_email:
                student_added_message_to_student(student, tutor)
            if student.parent and not student.with_email:
                student_added_message_to_parent(student, tutor)
            return HttpResponse(status=200)
        else:
            error['error'] = 'Ученик уже в списке ваших учеников'
            return JsonResponse(error, status=400)


class MyStudentsView(ListView):
    template_name = 'my_students.html'
    model = MyStudent

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MyStudentsView, self).get_context_data(object_list=object_list, **kwargs)
        tutor_cabinet = TutorCabinets.objects.get(id=self.kwargs['pk'])
        tutor = tutor_cabinet.user
        my_students = MyStudent.objects.filter(tutor_id=tutor.pk)
        # responses = Response.objects.filter(cabinet_tutor_id=tutor_cabinet.pk)
        # context['responses'] = responses
        context['my_students'] = my_students
        return context
