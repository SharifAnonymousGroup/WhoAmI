# Create your models here
from datetime import timedelta
import random
import string
import urllib
import sys

from django.http.response import HttpResponse

from UserManagement.models import *
from WhoAmI.settings import SITE_URL, NODE_URL


COLOR_CHOICES = (('r', 'red'), ('w', 'white'), ('g', 'green'), ('b', 'blue'), ('o', 'orange'),
                 ('y', 'yellow'), ('p', 'purple'), ('x', 'pink'), ('q', 'grey'), ('k', 'black'),
                 ('l', 'lightskyblue'), ('a', 'antiquewhite'), ('t', 'teal'), ('c', 'chocolate'),
                 ('d', 'darkgoldenrod'))


class PlayerManager(models.Manager):
    def create_player(self, member, game, color):
        player = self.model(member=member, game=game, color=color, isAlive=True, score=0,
                            isReady=False, loos_round=None)
        player.save()
        return player


class Player(models.Model):
    member = models.ForeignKey('UserManagement.Member', related_name='player')
    game = models.ForeignKey('Game', related_name='players')
    isAlive = models.BooleanField()
    score = models.IntegerField()
    color = models.CharField(max_length=1, choices=COLOR_CHOICES)
    isReady = models.BooleanField(default=False)
    loos_round = models.ForeignKey('Game.Round', null=True)
    # can_vote = models.BooleanField(default=1)
    # can_voted = models.BooleanField(default=1)
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
        game.number_of_ready_players = 0
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
    number_of_ready_players = models.IntegerField(default=0)
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
        # TODO color choises's size should be at lease max allowed player!!!!
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
        print >> sys.stderr, "player for " + member.username + \
                             " created and jont the game " + self.name + \
                             " by color " + player.color[1]

    def remove_member(self, member):
        self.players.get(member=member).delete()
        self.number_of_players -= 1
        self.save()

    def get_round_messages(self):
        messages = Message.objects.filter(round=self.current_round)
        return messages


    def goto_next_round(self):
        print "goto next round"
        turn = self.current_round.turn
        round = Round.objects.create_round(self, turn + 1, timezone.now())

        self.current_round = round
        self.save()

        # TODO bayad methodesh post beshe!
        params = urllib.urlencode({
            "round_duration": self.time_of_each_round,
            "election_duration": 20,
            "turn": turn,
            "room": self.code
        })
        url = NODE_URL + 'set_times/?%s' % params
        print "inja tehrane"
        urllib.urlopen(url)
        return HttpResponse()


    def __unicode__(self):
        return self.name


class MessageManager(models.Manager):
    def create_message(self, sender, round, text):
        message = self.model(sender=sender, round=round, text=text)
        # print text
        message.save()
        # print message
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

    def get_end_of_round(self):
        return self.start_time + timedelta.seconds(self.game.time_of_each_round)

    def calculate_result_of_election(self):  # TODO do the work
        votes = Vote.objects.filter(round=self)
        players = self.game.players
        for player in players:
            player.score = 0
        for vote in votes:
            if vote.color == eval(vote.target.color)[1]:
                vote.voter.score += 1
                vote.target.score -= 1
        mini = 1000
        looser = players[0]
        for player in players:
            if player.isAlive:
                if player.score < mini:
                    mini = player.score
        for player in players:
            if player.score == mini:
                player.isAlive = False
                player.save()
        print "scores"
        for player in players:
            print player.score

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
