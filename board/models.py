from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class EventCard(models.Model):
    users = models.ManyToManyField(User)   
    event_name = models.CharField(max_length=50)
    small_description = models.CharField(max_length=500)
    big_description = models.CharField(max_length=10000)
    date = models.DateTimeField('Data do Evento')
    room = models.CharField(max_length=200)

    def __str__(self):
        return self.event_name
    
    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk':self.pk})



class Task(models.Model):
    event = models.ForeignKey(EventCard, on_delete = models.CASCADE)
    description = models.CharField(max_length=200)
    users = models.ManyToManyField(User) 

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk':self.pk})

