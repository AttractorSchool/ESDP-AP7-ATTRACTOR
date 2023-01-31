import tempfile

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from cabinet_tutors.models import MyStudent
from reviews.models.reviews import Review
User = get_user_model()


class ReviewCase(TestCase):
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
        self.my_student = MyStudent.objects.create(tutor_id=self.user_1.pk, student_id=self.user_2.pk)

    def test_can_create_chat_message(self):
        self.client.post(reverse('make_review', kwargs={'pk': self.user_1.pk}),
                         {'tutor': self.user_1,
                          'author': self.user_2,
                          'rate': 5,
                          'text': 'Super tutor'}, follow=True)
        self.assertTrue(Review.objects.get(tutor_id=self.user_1.pk, text='Super tutor'))

    def tearDown(self):
        self.user_1.delete()
        self.user_2.delete()
        self.my_student.delete()
