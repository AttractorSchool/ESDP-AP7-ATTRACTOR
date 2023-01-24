from django.test import TestCase
from django.urls import reverse
import tempfile

from accounts.models import Account
from cabinet_parents.models import Survey
from cabinet_tutors.models import TutorCabinets
from responses.models import Response


class ResponseTestCase(TestCase):

    def setUp(self) -> None:
        self.user1 = Account.objects.create(
            email='testemail@gmail.com',
            username='testemail@gmail.com',
            password='password',
            first_name='first_name',
            last_name='last_name',
            father_name='father_name',
            type='student',
            phone='+77053456789',
            birthday='2023-01-21',
        )
        self.user1.save()

        self.user2 = Account.objects.create(
            email='testemail2@gmail.com',
            username='testemail2@gmail.com',
            password='password2',
            first_name='first_name2',
            last_name='last_name2',
            father_name='father_name2',
            type='tutor',
            phone='+77053456780',
            birthday='2023-01-21',
        )
        self.user2.save()

        self.login_url = reverse('login_page')
        self.credentials = {
            'username': self.user2.email,
            'password': self.user2.password}

        response = self.client.post(self.login_url, self.credentials, follow=True)

        self.tutor_cabinet = TutorCabinets.objects.create(gender='male', about='about', user=self.user2)
        self.survey = Survey.objects.create(min_cost=500, max_cost=1000, user=self.user1)

        user1 = Account.objects.first()
        user2 = Account.objects.last()

        self.response_on_tutor = Response.objects.create(author=user2,
                                                         cabinet_tutor=self.tutor_cabinet, hello_message='hello')

        self.response_on_student = Response.objects.create(author=user1,
                                                           survey=self.survey, hello_message='hello')

        self.response_on_student_url = reverse('response_on_student', args=[self.survey.pk])
        self.response_on_tutor_url = reverse('response_on_tutor', args=[self.tutor_cabinet.pk])
        self.response_from_parent_on_tutor_url = reverse('response_by_parent_on_tutor', args=[self.tutor_cabinet.pk])
        return super().setUp()

    def tearDown(self):
        self.user1.delete()
        self.user2.delete()
        self.response_on_tutor.delete()
        self.response_on_student.delete()


class TutorsTest(ResponseTestCase):

    def test_create_response_on_tutor_success(self):
        self.assertTrue(Response.objects.filter(cabinet_tutor=self.tutor_cabinet))

    def test_view_page_correctly(self):
        response = self.client.get(self.response_on_tutor_url)
        self.assertEqual(response.status_code, 302)
        # self.assertTemplateUsed(response, 'to_tutor_response_create.html')


class StudentsTest(ResponseTestCase):

    def test_create_response_on_student_success(self):
        self.assertTrue(Response.objects.filter(survey=self.survey))


    def test_view_page_correctly(self):
        response = self.client.get(self.response_on_student_url)
        self.assertEqual(response.status_code, 302)
        # self.assertTemplateUsed(response, 'to_student_response_create.html')

class ParentsTest(ResponseTestCase):

    def test_create_response_on_tutor_success(self):
        self.assertTrue(Response.objects.filter(cabinet_tutor=self.tutor_cabinet))


    def test_view_page_correctly(self):
        response = self.client.get(self.response_from_parent_on_tutor_url)
        self.assertEqual(response.status_code, 302)
        # self.assertTemplateUsed(response, 'to_tutor_response_create.html')

