# Create your models here
import random
import string
import urllib
import sys

from UserManagement.models import *
from WhoAmI.settings import SITE_URL



COLOR_CHOICES = (('r', 'red'), ('w', 'white'), ('g', 'green'), ('b', 'blue'), ('o', 'orange'),
                ('y', 'yellow'), ('p', 'purple'), ('x', 'pink'), ('q', 'grey'), ('k', 'black'),
                ('l', 'lightskyblue'), ('a', 'antiquewhite'), ('t', 'teal'), ('c', 'chocolate'),
                ('d','darkgoldenrod'))


class PlayerManager(models.Manager):
    def create_player(self, member, game, color):
        player = self.model(member=member, game=game, color=color, isAlive=True, score=0)
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

    def get_color(self):
        return eval(self.color)[1]


class GameManager(models.Manager):
    def create_game(self, name, time_of_each_round, max_number_of_players, creator):
        game = self.model(name=name, time_of_each_round=time_of_each_round,
                          max_number_of_players=max_number_of_players, creator=creator,
                          )
        game.is_active = True
        game.is_started = False
        game.number_of_players = 0
        game.code = game.create_code()
        game.save()
        round = Round.objects.create_round(game, 0, timezone.now())
        game.current_round = round
        return game


class Game(models.Model):
    time_of_each_round = models.IntegerField()  # in second
    current_players = models.IntegerField(default=0)
    max_number_of_players = models.IntegerField()
    creator = models.ForeignKey('UserManagement.Member')
    code = models.CharField(max_length=40)
    create_time = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField()
    is_started = models.BooleanField()
    name = models.CharField(max_length=30)
    number_of_players = models.IntegerField(default=0)
    current_round = models.ForeignKey('Round', null=True, related_name='current_game')
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

    def get_next_color(self):
        #TODO colar choises's size should be at lease max allowed player!!!!
        array = range(0, len(COLOR_CHOICES))
        random.shuffle(array)
        for x in array:
            try:
                self.players.get(color=COLOR_CHOICES[x])
            except:
                return COLOR_CHOICES[x]

    def have_member(self, member):
        try:
            Player.objects.get(game=self, member=member)
            return True
        except:
            return False

    def add_member(self, member):
        # zakhar (bolooke zakhar bayad pak she badan)
        player_list = member.player.all()
        # pr
        # int("salam bar to sag :|")
        for player in player_list:
            player.isAlive = False
            player.save()
        # end Of zAKHAR
        self.number_of_players += 1
        player = Player.objects.create_player(member=member, game=self, color=self.get_next_color())
        self.save()
        print >>sys.stderr, "player for " + member.username + \
                            " created and jont the game " + self.name + \
                            " by color " + player.color[1]

    def remove_member(self, member):
        self.players.get(member=member).delete()
        self.number_of_players -= 1
        self.save()

    def get_round_messages(self):
        messages = Message.objects.filter(round=self.current_round)
        return messages

    def __unicode__(self):
        return self.name


class MessageManager(models.Manager):
    def create_message(self, sender, round, text):
        message = self.model(sender=sender, round=round, text=text)
#        print text
        message.save()
#        print message
        return message


class Message(models.Model):
    sending_time = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey('Player', related_name='messages')
    round = models.ForeignKey('Round', related_name='messages', blank=True, null=True)
    text = models.TextField(max_length=250)
    objects = MessageManager()

    def __unicode__(self):
        color = eval(self.sender.color)
        return self.text


class RoundManager(models.Manager):
    def create_round(self, game, turn, start_time):
        round = self.model(game=game, turn=turn, start_time=start_time)
        round.save()
        return round


class Round(models.Model):
    game = models.ForeignKey('Game', related_name='rounds')
    turn = models.IntegerField()
    start_time = models.DateTimeField()
    objects = RoundManager()

    def __unicode__(self):
        return self.game.__unicode__() + " -> " + str(self.turn)


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
