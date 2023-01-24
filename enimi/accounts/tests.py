import tempfile
import time
from django.test import TestCase
from django.urls import reverse

from accounts.models import Account
from django.contrib.auth.models import User


class RegistrationTestCase(TestCase):
    def setUp(self) -> None:
        self.register_url = reverse('account_register', args=['type'])
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
        return super().setUp()


class RegisterTest(RegistrationTestCase):
    def test_view_page_correctly(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account_register.html')

    def test_can_register_user(self):
        user = Account.objects.get(id=self.user.pk)
        self.assertTrue(user)
        # self.assertEqual(Account.objects.count(), 1)

    # def tearDown(self):
    #     self.user.delete()


class LoginTestCase(RegistrationTestCase):

    def test_can_access_page(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_can_login_success(self):

        user = Account.objects.get(email=self.user.email)
        print(user)
        # self.client.login(username=self.user2.email, password=self.user2.password)
        # response = self.client.post(self.login_url, user, format='text/html')
        # self.assertEqual(response.status_code, 302)
        # self.client.login(username=user.username, password=user.password)

        self.user2 = Account.objects.create(
            email='testemail2@gmail.com',
            username='testemail2@gmail.com',
            password='password',
            first_name='first_name',
            last_name='last_name',
            father_name='father_name',
            type='type',
            avatar=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            phone='+77053456783',
            birthday='2023-01-21',
        )
        self.user2.save()
        self.credentials = {
            'username': 'testemail2@gmail.com',
            'password': 'password'}
        response = self.client.post(self.login_url, self.credentials, follow=True)
        # response = self.client.login(username=self.user.email, password='password')
        # print(response.content)
        # print(response.context['user'].is_authenticated)
        self.assertEqual(response.status_code, 302)


