import urllib

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render

from UserManagement.models import Member
from WhoAmI.settings import NODE_URL


__author__ = 'garfild'


@login_required
def chat(request):
    return render(request, 'chatUI/chat.html', {})


@login_required()
def send_message(request):
    user = Member(request.user)
    user = request.user
    player = user
    player = user.player.get(isAlive=True)
    print player
    room = player.game.code
    print "RE!"
    message = request.GET.get('message')
    print message
    # we must save this message
    params = urllib.urlencode({
        "message": message,
        "sender": player, #player.color,
        "room": room
    })

    f = urllib.urlopen(NODE_URL + '?%s' % params)
    #f.read()

    return HttpResponse("")
