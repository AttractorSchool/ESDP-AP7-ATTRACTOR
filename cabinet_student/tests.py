import tempfile

from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

from cabinet_student.forms import SurveyForm

User = get_user_model()
from django.test import TestCase

from django.urls import reverse

from accounts.models import Account
from cabinet_parents.models import Survey, Subject, Program, Test, EducationTime, OnlinePlatform, Region, City, District
from cabinet_tutors.models import MyStudent
from chat.models import Chat
from responses.models import Response


class StudentSurveyTestCase(TestCase):
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
        self.subject = Subject.objects.create(subject='Test')
        self.subject = Subject.objects.create(subject='Test')
        self.program = Program.objects.create(program='Test')
        self.test = Test.objects.create(test_name='Test')
        self.education_time = EducationTime.objects.create(education_time='Test')
        self.online = OnlinePlatform.objects.create(online_platform='Test')
        self.region = Region.objects.create(region='Test')
        self.city = City.objects.create(city='Test')
        self.district = District.objects.create(district='Test')
        self.client.login(username='testemail_1@gmail.com', password="password")
        # self.survey = Survey.objects.create(min_cost=500, max_cost=1000, user=self.user_2)

    def test_can_create_survey(self):
        self.response = self.client.post(reverse('student_create_survey', kwargs={'pk': self.user_1.pk}),
                                         {'min_cost': '500',
                                          'max_cost': '1500',
                                          'subjects': 1,
                                          'programs': 1,
                                          'tests': 1,
                                          'education_time': 1,
                                          'online': 1,
                                          'tutor_region': 1,
                                          'tutor_city': 1,
                                          'tutor_district': 1,
                                          'student_region': 1,
                                          'student_city': 1,
                                          'student_district': 1
                                          }, follow=True)
        self.assertTrue(Survey.objects.get(user_id=self.user_1.pk))

    def tearDown(self):
        self.user_1.delete()
