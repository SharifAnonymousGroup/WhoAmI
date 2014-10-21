from django.http.response import HttpResponse
from Game.models import Player
from UserManagement.models import Member

__author__ = 'po0ya'

#TODO naghese
def end(request):
    user = request.user
    member = Member(user)
    player = member.current_player
    if player is None:
        return HttpResponse('you not in this game')
#    player = Player.objects.get(member=member, isActive=True)
    game = player.game
    #TODO in mitune bug beshe. bayad age hame kharej shOdan is_active false beshe :)
    game.is_active = False
    member.current_player = None
    return HttpResponse('end of game...')