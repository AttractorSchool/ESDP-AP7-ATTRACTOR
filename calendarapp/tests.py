import tempfile

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from cabinet_tutors.models import TutorCabinets, MyStudent
from calendarapp.forms import EventForm, AddMemberForm

User = get_user_model()
from calendarapp.models import Event, EventMember


class EventTestCase(TestCase):
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
        self.tutor_cabinet = TutorCabinets.objects.create(user=self.user_1)

        self.response = self.client.login(username='testemail_1@gmail.com', password='password')
        self.event = Event.objects.create(user=self.user_1, title='title', description='description',
                                          start_time='2023-01-18 17:10:00.000000 +00:00',
                                          end_time='2023-01-18 17:10:00.000000 +00:00')

        self.event_member = EventMember.objects.create(event=self.event, user=self.user_2)


    def test_can_create_event(self):
        self.client.post(reverse('calendarapp:event_new'), {'user': self.user_1, 'title': 'title',
                                                            'description': 'description',
                                                            'start_time': '2023-01-18 17:10:00.000000 +00:00',
                                                            'end_time': '2023-01-18 17:10:00.000000 +00:00'},
                         follow=True)

        self.assertTrue(Event.objects.get(user=self.user_1))

    def test_can_add_member_to_event(self):
        # self.my_student = MyStudent.objects.create(tutor=self.user_1, student=self.user_2)
        # self.client.post(reverse('calendarapp:add_eventmember',
        #                          kwargs={'event_id': self.event.pk}),
        #                  {'user': self.user_2.pk}, follow=True)
        self.assertTrue(EventMember.objects.get(event=self.event, user=self.user_2))


#     def test_delete_not_exists_event_member(self):
#         response = self.client.post(reverse('calendarapp:remove_event', kwargs={'pk': 0}), follow=True)
#         self.assertEqual(404, response.status_code)

#     def test_delete_event(self):
#         response = self.client.post(reverse('calendarapp:event_delete', kwargs={'pk': self.event.pk}), follow=True)
#         self.assertEqual(200, response.status_code)
#         self.assertFalse(Event.objects.filter(pk=self.event.pk))

#     def test_delete_not_exists_event(self):
#         response = self.client.post(reverse('calendarapp:event_delete', kwargs={'pk': 0}), follow=True)
#         self.assertEqual(404, response.status_code)

#     def test_event_update_form(self):
#         form_data = {
#             'title': 'test_title',
#             'description': 'description1',
#             'start_time': '2023-01-18 17:10:00.000000 +00:00',
#             'end_time': '2023-01-19 17:10:00.000000 +00:00',
#         }
#         form = EventForm(data=form_data)
#         self.assertTrue(form.is_valid())

    # def test_update_event(self):
    #     self.response = self.client.login(username='testemail_1@gmail.com', password='password')
    #     self.client.force_login(self.user_1)
    #     event = Event.objects.get(id=self.event.pk)
    #     print(event.pk)
    #     print(event.title)
    #     form_data = {
    #         'title': 'test_title',
    #         'description': 'description1',
    #         'start_time': '2023-01-18 17:10:00.000000 +00:00',
    #         'end_time': '2023-01-19 17:10:00.000000 +00:00',
    #     }
    #     response = self.client.post(reverse('calendarapp:event_edit', kwargs={'pk': self.event.pk}),
    #                                 data=form_data)
    #
    #     self.assertEquals(response.status_code, 302)
    #     # self.event.title = 'test_title'
    #     self.event.save()
    #     self.event.refresh_from_db()
    #     self.assertEqual(event.title, 'test_title')

    def tearDown(self):
        self.user_1.delete()
        self.user_2.delete()
        self.event.delete()
        self.event_member.delete()
