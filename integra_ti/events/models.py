from django.db import models

class EventType(models.Model):
    name = models.CharField(max_length=100)

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    location = models.CharField(max_length=100)
    event_type = models.ForeignKey(EventType)

