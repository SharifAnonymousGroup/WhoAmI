from django.http.response import HttpResponse
from django.shortcuts import render

from Game.models import Game, Player
from UserManagement.models import Member


__author__ = 'Iman'


def room(request):
    print "user:"
    print request.user
    if request.method == 'GET':
        code = request.GET.get('code', '')

        if code != '':
            try:
                game = Game.objects.get(code=code)
                if not game.is_active:
                    return HttpResponse('your link is expired')
                if not game.have_member(Member(request.user)):
                    if len(Player.objects.filter(game=game)) < game.max_number_of_players:
                        game.add_member(Member(request.user))
                        print "player is created"
                        # return HttpResponse

                        return render(request, 'chatUI/chat.html', {'room': code})
                    else:
                        return HttpResponse('room is full!')
                else:
                    # return HttpResponse('you successfully joined to the game')
                    print "player is not craeted"
                    return render(request, 'chatUI/chat.html', {'room': code})
            except Game.DoesNotExist:
                return HttpResponse('Your url is not valid')
        else:
            return HttpResponse('Your url is not valid')
    else:
        return HttpResponse('Your request was not get')