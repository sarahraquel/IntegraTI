from django.test import TestCase
from events.models import Event
from rest_framework import status

class EventModelTest(TestCase):
    def setUp(self):
        self.event = Event(name="Test Event")

    def test_model_can_create_a_event(self):
        old_count = Event.objects.count()
        self.event.save()
        new_count = Event.objects.count()
        self.assertNotEqual(old_count, new_count)
