from django.http.response import HttpResponse
from Game.models import Player

__author__ = 'po0ya'

#TODO naghese
def end(request):
    member = request.user
#    player = Player.objects.get(member=member, isActive=True)
    game = player.game
    game.is_active = False
    return HttpResponse('end of game...')