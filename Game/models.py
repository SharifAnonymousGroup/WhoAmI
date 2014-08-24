from django.db import models

# Create your models here.
from UserManagement.models import *


class Player(models.Model):
    member = models.ForeignKey('UserManagement.Member', related_name='player')
    room = models.ForeignKey('Room', related_name='players')
    isAlive = models.IntegerField()
    score = models.IntegerField()


class Room(models.Model):
    timeOfEachTurn = models.IntegerField()
    maxNumberOfPlayer = models.IntegerField()
    creator = models.ForeignKey('UserManagement.Member')
    url = models.CharField(max_length=10)
    turn = models.IntegerField()