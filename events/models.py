from django.db import models
from django.conf import settings
from django.utils import timezone


class Event(models.Model):
    name = models.CharField(max_length=255, default="")
    description = models.TextField(default="")  
    location = models.CharField(max_length=255, default="")
    event_date = models.DateField(null=True, default=None)
    creation_date = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=None) 
    photo_url = models.URLField(max_length=200, null=True)


    def __str__(self):
        return f'{self.name} ({self.event_date})'