# Create your models here
import random
import string
import urllib

from UserManagement.models import *
from WhoAmI.settings import SITE_URL


COLOR_CHOICES = ( ('r', 'red'), ('w', 'white'), ('g', 'green'), ('b', 'blue'), ('o', 'orange'),
                  ('y', 'yellow'), ('p', 'purple'), ('x', 'pink'), ('q', 'grey'))


class PlayerManager(models.Manager):
    def create_player(self, member, game):
        print member.username
        print game.name
        player = self.model(member=member, game=game, color=COLOR_CHOICES[0], isAlive=True, score=0)
        player.save()
        return player


class Player(models.Model):
    member = models.ForeignKey('UserManagement.Member', related_name='player')
    game = models.ForeignKey('Game', related_name='players')
    isAlive = models.BooleanField()
    score = models.IntegerField()
    color = models.CharField(max_length=1, choices=COLOR_CHOICES)
    objects = PlayerManager()


    def __unicode__(self):
        return self.member.__unicode__() + " " + str(self.isAlive)


class GameManager(models.Manager):
    def create_game(self, name, time_of_each_round, max_number_of_players, creator):
        game = self.model(name=name, time_of_each_round=time_of_each_round,
                          max_number_of_players=max_number_of_players, creator=creator)
        print 'salam'
        game.is_active = True
        game.is_started = False
        game.code = game.create_code()
        game.save()
        return game


class Game(models.Model):
    time_of_each_round = models.IntegerField()  # in second
    max_number_of_players = models.IntegerField()
    creator = models.ForeignKey('UserManagement.Member')
    code = models.CharField(max_length=40)
    create_time = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField()
    is_started = models.BooleanField()
    name = models.CharField(max_length=30)
    objects = GameManager()

    def create_code(self):
        chars = string.ascii_letters + string.digits
        size = 40
        return ''.join(random.choice(chars) for _ in range(size))

    def get_url(self):
        params = urllib.urlencode({
            "code": self.code,
        })
        return SITE_URL + 'game/rooms/?' + params

    def have_member(self, member):
        try:
            Player.objects.get(game=self, member=member)
            return True
        except:
            return False

    def add_member(self, member):
        # zakhar (bolooke zakhar bayad pak she badan)
        player_list = Player.objects.filter(member=member)
        for player in player_list:
            player.isAlive = False
            player.save()
            print "salam"
        # end Of zAKHAR
        Player.objects.create_player(member=member, game=self)
        print "player created!"

    def __unicode__(self):
        return self.name


class MessageManager(models.Model):
    def create_message(self, sender, round, text):
        message = self.model(sender=sender, round=round, text=text)
        message.save()
        return message


class Message(models.Model):
    sending_time = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey('Player', related_name='messages')
    round = models.ForeignKey('Round', related_name='messages')
    text = models.TextField(max_length=250)
    objects = MessageManager


class RoundManager(models.Manager):
    def create_round(self, game, turn):
        round = self.model(game=game, turn=turn)
        round.save()
        return round


class Round(models.Model):
    game = models.ForeignKey('Game', related_name='rounds')
    turn = models.IntegerField()
    objects = RoundManager()


class VoteManager(models.Manager):
    def create_vote(self, round, voter, color, target):
        vote = self.model(round=round, voter=voter, color=color, target=target)
        vote.save()
        return vote


class Vote(models.Model):
    round = models.ForeignKey('Round', related_name='votes')
    voter = models.ForeignKey('Player', related_name='votes')
    color = models.CharField(choices=COLOR_CHOICES, max_length=1)
    target = models.ForeignKey('Player', related_name='voted-to', null=True)
    objects = VoteManager()