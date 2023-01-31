import tempfile

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from cabinet_parents.models import Survey
from cabinet_tutors.models import TutorCabinets
from chat.models import Chat
from responses.models import Response

User = get_user_model()


class ChatCase(TestCase):
    def setUp(self) -> None:
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
        self.response = self.client.login(username='testemail_1@gmail.com', password='password')
        # self.tutor_cabinet = TutorCabinets.objects.create(user=self.user_1)
        self.survey = Survey.objects.create(min_cost=500, max_cost=1000, user=self.user_2)
        self.user_response = Response.objects.create(hello_message='hello_message', survey=self.survey, author=self.user_1)

    def test_can_create_chat_message(self):
        self.client.post(reverse('add_chat_message', kwargs={'pk': self.user_response.pk}),
                                          {'message': 'message',
                                           'response_id': self.user_response,
                                           'author_id': self.user_1.pk}, follow=True)
        self.assertTrue(Chat.objects.get(author_id=self.user_1.pk, response=self.user_response))

    def tearDown(self):
        self.user_1.delete()
        self.user_2.delete()
        self.survey.delete()
