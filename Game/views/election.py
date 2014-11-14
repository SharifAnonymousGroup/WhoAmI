import json

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse

from Game.models import Player


__author__ = 'garfild'


@login_required
def election(request):
    user = request.user

    # player = user.current_player
    player = Player.objects.get(member=user, isAlive=True)
    if player is None:
        return HttpResponse("you was not in this room")
    game = player.game

    players = Player.objects.filter(game=game, isAlive=True)
    print players
    print game.name
    colors = [eval(player.color)[1] for player in players]
    players = [player.member.username for player in players]
    json_players = json.dumps(players)
    dic = {'colors': colors, 'json_players': json_players, 'players': players}
    # print players
    return dic


def election_request(request):
    print "election recieved"
    print "zakhar biya"
    user = request.user.username
    if request.method == 'POST':
        print "zakhar"
        print request.POST[user]
    return HttpResponse()