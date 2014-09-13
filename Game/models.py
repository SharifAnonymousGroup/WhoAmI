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

    def __init__(self, member, game, color):
        super(Player, self).__init__()
        self.member = member
        self.game = game
        self.color = color
        self.isAlive = True
        self.score = 0
        self.save()


class Game(models.Model):
    time_of_each_round = models.IntegerField() # in second
    max_number_of_player = models.IntegerField()
    creator = models.ForeignKey('UserManagement.Member')
    code = models.CharField(max_length=30)
    round = models.ForeignKey('Round',related_name='current_round', null=True)
    create_time = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField()
    is_started = models.BooleanField()
    name = models.CharField(max_length=30)

    def __init__(self, name, time_of_each_round, max_number_of_player, creator):
        super(Game, self).__init__()
        self.time_of_each_round = time_of_each_round
        self.max_number_of_player = max_number_of_player
        print 'start new game'
        print creator.username + " " + creator.get_full_name()
        self.creator = creator
        self.turn = 0
        self.is_active = True
        self.is_started = False
        self.name = name
        self.save()

    #Todo
    def create_code(self):
        pass


class Message(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey('Player', related_name='messages')
    round = models.ForeignKey('Round', related_name='messages')
    text = models.TextField(max_length=250)

    def __init__(self, sender, round, text):
        super(Message, self).__init__()
        self.sender = sender
        self.round = round
        self.text = text
        self.save()


class Round(models.Model):
    game = models.ForeignKey('Game', related_name='rounds')

    def __init__(self, game):
        super(Round, self).__init__()
        self.game = game
        self.save()


class Vote(models.Model):
    round = models.ForeignKey('Round', related_name='votes')
    voter = models.ForeignKey('Player', related_name='votes')
    color = models.CharField(choices=COLOR_CHOICES, max_length=1)
    target = models.ForeignKey('Player', related_name='voted-to', null=True)

    def __init__(self, round, voter, color, target):
        super(Vote, self).__init__()
        self.round = round
        self.voter = voter
        self.color = color
        self.target = target
        self.save()