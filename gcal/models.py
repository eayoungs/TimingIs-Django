from django.db import models
from django.contrib.auth.models import User


class CalEvent(models.Model):
    # https://developers.google.com/google-apps/calendar/v3/reference/events
    def description_default():
        return "Description of this event"

    description = models.TextField("Event Description", default=description_default) 
