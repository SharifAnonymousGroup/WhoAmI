# Create your models here

from UserManagement.models import *

COLOR_CHOICES = ( ('r', 'red'), ('w', 'white'), ('g', 'green'), ('b', 'blue'), ('o', 'orange'),
                  ('y', 'yellow'), ('p', 'purple'), ('x', 'pink'), ('q', 'grey'))


class Player(models.Model):
    member = models.ForeignKey('UserManagement.Member', related_name='player')
    game = models.ForeignKey('Game', related_name='players')
    isAlive = models.BooleanField()
    score = models.IntegerField()
    color = models.CharField(max_length=1, choices=COLOR_CHOICES)


class Game(models.Model):
    time_of_each_round = models.IntegerField()  # in second
    max_number_of_player = models.IntegerField()
    creator = models.ForeignKey('UserManagement.Member')
    code = models.CharField(max_length=30)
    create_time = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField()
    is_started = models.BooleanField()
    name = models.CharField(max_length=30)


    # Todo
    def create_code(self):
        pass


class Message(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey('Player', related_name='messages')
    round = models.ForeignKey('Round', related_name='messages')
    text = models.TextField(max_length=250)


class Round(models.Model):
    game = models.ForeignKey('Game', related_name='rounds')
    turn = models.IntegerField()


class Vote(models.Model):
    round = models.ForeignKey('Round', related_name='votes')
    voter = models.ForeignKey('Player', related_name='votes')
    color = models.CharField(choices=COLOR_CHOICES, max_length=1)
    target = models.ForeignKey('Player', related_name='voted-to', null=True)