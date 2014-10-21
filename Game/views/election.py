import json

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse

from Game.models import Player


__author__ = 'garfild'


@login_required
def election(request):
    user = request.user

    # player = user.current_player
    print "zakhara"
    player = Player.objects.get(member=user, isAlive=True)
    if player is None:
        return HttpResponse("you was not in this room")
    game = player.member
    print user.username

    players = Player.objects.filter(game=game, isAlive=True)
    colors = [eval(player.color)[1] for player in players]
    players = [player.member.username for player in players]
    json_players = json.dumps(players)
    dic = {'colors': colors, 'json_players': json_players, 'players': players}
    return dic


def election_request():
    pass