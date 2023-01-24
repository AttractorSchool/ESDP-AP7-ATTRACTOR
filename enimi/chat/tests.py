import tempfile

from django.test import TestCase
from django.urls import reverse

from accounts.models import Account
from cabinet_parents.models import Survey
from chat.models import Chat
from responses.models import Response


class ChatTestCase(TestCase):
    def setUp(self) -> None:
        self.login_url = reverse('login_page')
        self.user = Account.objects.create(
            email='testemail@gmail.com',
            username='testemail@gmail.com',
            password='password',
            first_name='first_name',
            last_name='last_name',
            father_name='father_name',
            type='type',
            avatar=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            phone='+77053456789',
            birthday='2023-01-21',
        )
        self.user.save()
        self.user = Account.objects.get(email=self.user.email)
        self.credentials = {
            'username': self.user.email,
            'password': self.user.password,
            'next': ''}
        response = self.client.post(self.login_url, self.credentials, follow=True)
        print(response.context['user'].is_authenticated)
        self.assertEqual(response.status_code, 200)

        response = self.client.login(username=self.user.email, password=self.user.password)
        print(self.client.login(username=self.user.email, password=self.user.password))

        self.survey = Survey.objects.create(min_cost=500, max_cost=1000, user=self.user)
        self.response = Response.objects.create(author=self.user,
                                                survey=self.survey, hello_message='hello')

        self.add_chat_message_url = reverse('add_chat_message', args=[self.response.pk])

        return super().setUp()


class ChatTest(ChatTestCase):
    def test_view_page_correctly(self):

        response = self.client.get(self.add_chat_message_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'response_chat.html')

    def test_can_create_message_user(self):
        self.chat = Chat.objects.create(message='hello', author=self.user, response=self.response)
        self.assertEqual(Chat.objects.count(), 1)

    def tearDown(self):
        self.user.delete()


# class ChatTestView(ChatTestCase):
#     def test_can_create_message_view(self):
#
#         response = self.client.post(self.add_chat_message_url, data={'message': 'foo', 'author': self.user,
#                                                                       'response': self.response})
#         self.assertEqual(Chat.objects.count(), 1)
