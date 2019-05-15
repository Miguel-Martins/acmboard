from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.exceptions import ValidationError
# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=200, default = ' ')
    image = models.ImageField(default='default-board.jpg', upload_to='board-imgs')

    def __str__(self):
        return self.name


class EventCard(models.Model):
    users = models.ManyToManyField(User)   
    event_name = models.CharField(max_length=50)
    small_description = models.CharField(max_length=500,default=' ')
    big_description = models.CharField(max_length=10000,default=' ')
    date = models.DateTimeField()
    room = models.CharField(max_length=200)
    board = models.ForeignKey(Board, on_delete = models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.event_name
    
    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk':self.pk})

    def get_percentage(self):
        percentage = 0
        totalTasks = self.task_set.all().count()
        completedTasks = self.task_set.all().filter(isCompleted=True).count()
        if totalTasks > 0:
            percentage = completedTasks / totalTasks *100

        return percentage




class Attachment(models.Model):
    file = models.FileField(upload_to='attachment_files', null=False, blank=True)
    event = models.ForeignKey(EventCard, on_delete = models.CASCADE, null=True, blank=True)

    def clean(self):
        if not self.file.name:
            raise ValidationError('Error With File')

class Task(models.Model):
    event = models.ForeignKey(EventCard, on_delete = models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=200)
    users = models.ManyToManyField(User) 
    isCompleted = models.BooleanField(default = False)

    def __str__(self):
        return self.description
