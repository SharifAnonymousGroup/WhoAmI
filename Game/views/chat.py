import urllib

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render

from Game.models import Player, Message, Game
from UserManagement.models import Member


__author__ = 'garfild'


@login_required
def chat(request):
    return render(request, 'chatUI/chat.html', {})


@login_required()
def send_message(request):
    user = request.user
    member = Member(user)
    player = member.current_player
    if player is None:
        return HttpResponse('you cant send message in this room!')

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


@login_required
def leave_game(request):
    user = request.user
    member = Member(user)
    player = member.current_player
    if player is None:
        return HttpResponse("You was not in this room")
    game = player.game
    game.remove_member(user)
    return HttpResponse('you removed from game')
