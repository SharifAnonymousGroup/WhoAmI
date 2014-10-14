import urllib

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render

from Game.models import Player, Message


__author__ = 'garfild'


@login_required
def chat(request):
    return render(request, 'chatUI/chat.html', {})


@login_required()
def send_message(request):
    user = request.user
    player = Player.objects.get(member=user, isAlive=True)

    room = player.game.code
    message = request.GET.get('message')
    Message.objects.create_message(sender=player, text=message, round=None)
    color = eval(player.color)
    print color[1]

    params = urllib.urlencode({
        "message": message,
        "sender": color[1],
        "room": room
    })
    url = 'http://localhost:3333/?%s' % params
    urllib.urlopen(url)
    return HttpResponse()
