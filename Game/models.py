from django.db import models

# Create your models here.
from UserManagement.models import *


class Player(models.Model):
    member = models.ForeignKey('Member', related_name='player')
    room = models.ForeignKey('Room', related_name='players')
    isAlive = models.IntegerField()
    score = models.IntegerField()


class Room(models.Model):
    timeOfEachTurn = models.IntegerField()
    maxNumberOfPlayer = models.IntegerField()
    creator = models.ForeignKey('Member')
    url = models.CharField()
    turn = models.IntegerField()