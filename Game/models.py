# Create your models here

from UserManagement.models import *

COLOR_CHOICES = ( ('r', 'red'), ('w', 'white'), ('g', 'green'), ('b', 'blue'), ('o', 'orange'),
                  ('y', 'yellow'), ('p', 'purple'), ('x', 'pink'), ('q', 'grey'))

class Player(models.Model):
    member = models.ForeignKey('UserManagement.Member', related_name='player')
    room = models.ForeignKey('Room', related_name='players')
    isAlive = models.BooleanField()
    score = models.IntegerField()
    color = models.CharField(max_length=1, choices=COLOR_CHOICES)

class Room(models.Model):
    timeOfEachTurn = models.IntegerField() # in second
    maxNumberOfPlayer = models.IntegerField()
    creator = models.ForeignKey('UserManagement.Member')
    #url = models.CharField(max_length=10)
    turn = models.IntegerField()

class Message(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    player = models.ForeignKey('Player', related_name='messages')
    room = models.ForeignKey('Room', related_name='rooms')
    text = models.TextField(max_length=250)

#class Round(models.Model):
 #   room = models.ForeignKey('Room', related_name='rooms')