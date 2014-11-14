import urllib

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render

from Game.models import Player, Message
from WhoAmI.settings import NODE_URL


__author__ = 'garfild'


@login_required
def chat(request):
    return render(request, 'chatUI/chat.html', {})


@login_required()
def send_message(request):
    user = request.user
    player = Player.objects.get(member=user, isAlive=True)  # TODO exception handeling
    room = player.game.code
    message = request.GET.get('message')
    Message.objects.create_message(sender=player, text=message, round=player.game.current_round)
    color = eval(player.color)  # TODO mishe bedoone eval zadesh chon code python ejra mishe gand mizane

    # TODO bayad methodesh post beshe!
    params = urllib.urlencode({
        "message": message,
        "sender": color[1],
        "room": room
    })
    url = NODE_URL + 'message/?%s' % params

    urllib.urlopen(url)
    return HttpResponse()


@login_required
def leave_game(request):
    user = request.user
    player = Player.objects.get(member=user, isAlive=True)
    game = player.game
    game.remove_member(user)
    return HttpResponse('you removed from game')
