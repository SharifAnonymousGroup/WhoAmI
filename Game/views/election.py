import json

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render

from Game.models import Player
from UserManagement.models import Member


__author__ = 'garfild'


@login_required
def election(request):
    user = request.user
    member = Member(user)
    player = member.current_player
    if player is None:
        return HttpResponse("you was not in this room")
    #player = Player.objects.get(member=user, isAlive=True)
    game = player.game
    print user.username

    players = Player.objects.filter(game=game, isAlive=True)
    colors = [eval(player.color)[1] for player in players]
    players = [player.member.username for player in players]
    json_players = json.dumps(players)

    return render(request, 'test/election.html', {'colors': colors, 'json_players': json_players, 'players': players})