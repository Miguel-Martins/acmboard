from django.db import models

# Create your models here.
class EventCard(models.Model):
    description = models.CharField(max_length=10000)
    date = models.DateTimeField('Data do Evento')
    room = models.CharField(max_length=200)

    def __str__(self):
        return self.description


class Tasks(models.Model):
    event = models.ForeignKey(EventCard, on_delete = models.CASCADE)
    description = models.CharField(max_length=200)
    ##Suponho que devamos ter um user associado a tarefs também

    def __str__(self):
        return self.description
