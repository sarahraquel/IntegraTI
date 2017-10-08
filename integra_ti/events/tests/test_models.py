from django.test import TestCase
from events.models import Event, EventType
from rest_framework import status

class EventTypeModelTest(TestCase):
    def setUp(self):
        self.event_type = EventType(name="Test Event type")

    def test_model_can_create_a_event(self):
        old_count = EventType.objects.count()
        self.event_type.save()
        new_count = EventType.objects.count()
        self.assertNotEqual(old_count, new_count)

class EventModelTest(TestCase):
    def setUp(self):
        self.event_type = EventType.objects.create(name="Event type example")
        self.event = Event(title="Test Event", location="IMD", description="Description example", event_type=self.event_type)

    def test_model_can_create_a_event(self):
        old_count = Event.objects.count()
        self.event.save()
        new_count = Event.objects.count()
        self.assertNotEqual(old_count, new_count)


