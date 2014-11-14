from datetime import timedelta
import urllib

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from Game.models import Player, Message, Game


__author__ = 'garfild'


@login_required
def chat(request):
    return render(request, 'chatUI/chat.html', {})


@login_required()
def send_message(request):
    user = request.user
    try:
        player = Player.objects.get(member=user, isAlive=True)
    except:
        HttpResponse("You are not join to a Game")
    game = player.game
    if timezone.now() <= game.current_round.start_time + timedelta.seconds(game.time_of_each_round):
        room = player.game.code
        message = request.GET.get('message')
        Message.objects.create_message(sender=player, text=message, round=player.game.current_round)
        color = eval(player.color)#TODO mishe bedoone eval zadesh chon code python ejra mishe gand mizane

        #TODO bayad methodesh post beshe!
        params = urllib.urlencode({
            "message": message,
            "sender": color[1],
            "room": room
        })
        url = 'http://localhost:3333/?%s' % params
        urllib.urlopen(url)
        return HttpResponse()
    else:
        HttpResponse("Chat is finished")



@login_required
def leave_game(request):
    user = request.user
    player = Player.objects.get(member=user, isAlive=True)
    game = player.game
    game.remove_member(user)
    return HttpResponse('you removed from game')
