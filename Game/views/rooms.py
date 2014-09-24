from django.http.response import HttpResponse
from django.shortcuts import render

from Game.models import Game, Player, Message


__author__ = 'Iman'


def room(request):
    print "umad injahaaaa"
    if request.method == 'GET':
        code = request.GET.get('code', '')
        if code != '':
            try:
                print "inja ke nemikhaim umad!"
                game = Game.objects.get(code=code)
                if not game.is_active:
                    return HttpResponse('your link is expired')
                if not game.have_member(request.user):
                    print "inja ke mikhaim umad!"
                    if len(Player.objects.filter(game=game)) < game.max_number_of_players:
                        game.add_member(request.user)

                        # return HttpResponse

                        return render(request, 'chatUI/chat.html', {'room': code, 'message': current_message(game)})
                    else:
                        return HttpResponse('room is full!')
                else:
                    return render(request, 'chatUI/chat.html', {'room': code, 'message': current_message(game)})
            except Game.DoesNotExist:
                return HttpResponse('Your url is not valid')
        else:
            return HttpResponse('Your url is not valid')
    else:
        return HttpResponse('Your request was not get')


def current_message(game):
    return Message.objects.filter(game=game)