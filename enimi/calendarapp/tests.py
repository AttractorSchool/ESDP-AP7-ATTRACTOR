import tempfile

from django.test import TestCase
from django.urls import reverse

from accounts.models import Account
from cabinet_parents.models import Survey
from cabinet_tutors.models import MyStudent
from calendarapp.models import Event, EventMember
from chat.models import Chat
from responses.models import Response


class EventTestCase(TestCase):
    def setUp(self) -> None:

        self.user = Account.objects.create(
            email='testemail@gmail.com',
            username='testemail@gmail.com',
            password='password',
            first_name='first_name',
            last_name='last_name',
            father_name='father_name',
            type='type',
            # avatar=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            phone='+77053456789',
            birthday='2023-01-21',
        )
        self.user2 = Account.objects.create(
            email='testemail1@gmail.com',
            username='testemail1@gmail.com',
            password='password',
            first_name='first_name',
            last_name='last_name',
            father_name='father_name',
            type='type',
            # avatar=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            phone='+77053456781',
            birthday='2023-01-21',
        )
        self.user2.save()
        self.user = Account.objects.get(email=self.user.email)
        self.user2 = Account.objects.get(email=self.user2.email)

        self.event = Event.objects.create(user=self.user, title='title', description='description',
                                          start_time='2023-01-18 17:10:00.000000 +00:00',
                                          end_time='2023-01-18 17:10:00.000000 +00:00')

        # self.event_add_member_url = reverse('add_eventmember', kwargs={'pk': self.event.pk})

        return super().setUp()


class AddEventTest(EventTestCase):

    def test_can_create_message_user(self):
        self.assertEqual(Event.objects.count(), 1)

    def tearDown(self):
        self.user.delete()


class AddMemberToEventTest(EventTestCase):

    def test_can_add_member_to_event(self):
        event = Event.objects.get(title='title')
        EventMember.objects.create(event=event, user=self.user2)
        self.assertEqual(EventMember.objects.count(), 1)

    # def test_can_add_member_page(self):
    #     response = self.client.get(self.event_add_member_url)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'add_member.html')
