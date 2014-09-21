import urllib

from django.contrib.auth.decorators import login_required

from django.http.response import HttpResponse
from django.shortcuts import render

from Game.models import Player
from WhoAmI.settings import NODE_URL


__author__ = 'garfild'


@login_required
def chat(request):
    return render(request, 'chatUI/chat.html', {})


@login_required()
def send_message(request):
    # user = Member(request.user)
    user = request.user
    player = Player.objects.filter(member=user, isAlive=True)[0]
    room = player.game.code
    message = request.GET.get('message')
    # we must save this message
    params = urllib.urlencode({
        "message": message,
        "sender": player.color,
        "room": room
    })
    url = 'http://localhost:3333/?%s' % params
    f = urllib.urlopen(url)

    return HttpResponse("")
