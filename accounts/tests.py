import tempfile

from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
User = get_user_model()
from django.test import TestCase

# from django.contrib.auth.models import User

from django.urls import reverse

from accounts.models import Account


class UserRegisterTest(TestCase):
    def setUp(self):
        self.register_url = reverse('account_register', args=['type'])
        self.login_url = reverse('login_page')
        self.user = User.objects.create_user(
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

    def test_view_page_correctly(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account_register.html')

    def test_can_register_user(self):
        user = User.objects.get(id=self.user.pk)
        self.assertTrue(self.user)
        self.assertEqual(Account.objects.count(), 1)



    def tearDown(self):
        self.user.delete()


class UserLoginTest(TestCase):
    def setUp(self):
        self.register_url = reverse('account_register', args=['type'])
        self.login_url = reverse('login_page')
        self.user = User.objects.create_user(
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
        self.credentials = {
            'username': 'testemail@gmail.com',
            'password': 'password'}
        self.response = self.client.login(username='testemail@gmail.com', password='password')

    def test_can_access_page(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_user_can_login(self):
        response = self.client.post('/auth/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)


    def tearDown(self):
        self.user.delete()
