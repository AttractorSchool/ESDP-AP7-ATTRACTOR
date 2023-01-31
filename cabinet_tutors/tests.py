import tempfile

from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
User = get_user_model()
from django.test import TestCase

from django.urls import reverse

from accounts.models import Account
from cabinet_parents.models import Survey, Subject
from cabinet_tutors.models import MyStudent
from chat.models import Chat
from responses.models import Response

class StudentAddTestCase(TestCase):
    def setUp(self):
        self.user_1 = User.objects.create_user(
            email='testemail_1@gmail.com',
            username='testemail_1@gmail.com',
            password='password',
            first_name='first_name',
            last_name='last_name',
            father_name='father_name',
            type='type',
            avatar=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            phone='+77053456789',
            birthday='2023-01-21',
        )
        self.user_1.save()

        self.user_2 = User.objects.create_user(
            email='testemail_2@gmail.com',
            username='testemail_2@gmail.com',
            password='password',
            first_name='first_name',
            last_name='last_name',
            father_name='father_name',
            type='type',
            avatar=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            phone='+77053456789',
            birthday='2023-01-21',
        )
        self.user_2.save()

        self.client.login(username='testemail_1@gmail.com', password="password")
        self.survey = Survey.objects.create(min_cost=500, max_cost=1000, user=self.user_2)
        self.subject = Subject.objects.create(subject='География')
        self.response = Response.objects.create(author=self.user_1,
                                                survey=self.survey, hello_message='hello')
        self.my_student = MyStudent.objects.create(tutor=self.user_1, student=self.user_2)
        # self.add_student_to_tutor_list_url = reverse('add_user_to_my_students', args=[self.response.survey.user.pk])


    def test_can_create_survey(self):
        self.assertTrue(Survey.objects.get(user_id=self.user_2.pk))

    def test_can_create_response(self):
        # self.response = self.client.post(reverse('response_on_student', kwargs={'pk': self.survey.pk}), {'hello_message': 'message',
        #                                                    'subjects': Subject.objects.first()}, follow=True)
        # print(Response.objects.all())
        self.assertTrue(Response.objects.get(author_id=self.user_1.pk, survey=self.survey.pk))

    def test_can_add_to_tutors_student_list(self):
        self.responses = self.client.get(reverse('add_user_to_my_students', kwargs={'pk': self.user_2.pk}))
        self.assertTrue(MyStudent.objects.get(tutor_id=self.user_1.pk, student_id=self.user_2.pk))

    def tearDown(self):
        self.user_1.delete()
        self.user_2.delete()
        self.survey.delete()
        self.subject.delete()
        # self.responses.delete()
        self.my_student.delete()
