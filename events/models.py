from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User


class Event(models.Model):
    name = models.CharField(max_length=255, default="")
    description = models.TextField(default="")  
    location = models.CharField(max_length=255, default="")
    event_date = models.DateField(null=True, default=None)
    creation_date = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=None) 
    photo_url = models.URLField(max_length=200, null=True)


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    post_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'

    def __str__(self):
        return f'{self.name} ({self.event_date})'
    
class Perfil(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio = models.TextField()
    telefone = models.CharField(null=True, blank=True,max_length=11)
    whatsapp = models.CharField(null=True, blank=True,max_length=11)
    instagram = models.CharField(null=True, blank=True,max_length=25)    

class Category(models.Model):
    name = models.CharField(max_length=255)
    content = content = models.TextField() 
    events = models.ManyToManyField(Event)

    def __str__(self):
        return f'{self.name}'