from django.test import TestCase
from django.urls import reverse

from accounts.models import Account

class BoardsTestCase(TestCase):
    def setUp(self) -> None:
        self.tutors_url = reverse('board_tutor')
        self.students_url = reverse('board_student')
        return super().setUp()

class TutorsTest(BoardsTestCase):
    def test_view_page_correctly(self):
        response = self.client.get(self.tutors_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'board_tutor.html')


# class StudentsTest(BoardsTestCase):
#     def test_view_page_correctly(self):
#         response = self.client.get(self.students_url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'board_student.html')
