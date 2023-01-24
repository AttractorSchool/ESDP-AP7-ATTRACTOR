import tempfile

from django.test import TestCase
from django.urls import reverse

from accounts.models import Account
from cabinet_parents.models import Survey
from cabinet_tutors.models import MyStudent
from chat.models import Chat
from responses.models import Response

class StudentAddTestCase(TestCase):
    def setUp(self) -> None:
        self.login_url = reverse('login_page')
        self.user = Account.objects.create(
            email='testemail@gmail.com',
            username='testemail@gmail.com',
            password='password',
            first_name='first_name',
            last_name='last_name',
            father_name='father_name',
            type='tutor',
            avatar=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            phone='+77053456789',
            birthday='2023-01-21',
        )
        self.user.save()
        self.user2 = Account.objects.create(
            email='testemail2@gmail.com',
            username='testemail2@gmail.com',
            password='password',
            first_name='first_name',
            last_name='last_name',
            father_name='father_name',
            type='student',
            avatar=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            phone='+77053456784',
            birthday='2023-01-21',
        )
        self.user2.save()

        self.user = Account.objects.get(email=self.user.email)
        self.credentials = {
            'username': self.user.email,
            'password': self.user.password,
            'next': ''}
        response = self.client.post(self.login_url, self.credentials, follow=True)
        print(response.context['user'].is_authenticated)
        self.assertEqual(response.status_code, 200)

        self.survey = Survey.objects.create(min_cost=500, max_cost=1000, user=self.user2)
        self.response = Response.objects.create(author=self.user,
                                                survey=self.survey, hello_message='hello')

        my_student = MyStudent.objects.create(tutor=self.user, student=self.user2)

        self.add_student_to_tutor_list_url = reverse('add_user_to_my_students', args=[self.response.survey.user.pk])

        return super().setUp()


class AddStudentTest(StudentAddTestCase):

    def test_can_create_message_user(self):
        self.assertEqual(MyStudent.objects.count(), 1)

    def tearDown(self):
        self.user.delete()
        self.user2.delete()
