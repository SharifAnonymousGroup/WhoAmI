from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render

from Game.models import Game, Player


__author__ = 'Iman'

@login_required
def room(request):
    if request.method == 'GET':
        code = request.GET.get('code', '')
        if code != '':
            try:
                game = Game.objects.get(code=code)
                if not game.is_active:
                    return HttpResponse('your link is expired')
                if not game.have_member(request.user):
                    if game.number_of_joint_players < game.max_number_of_players and not game.is_started:
                        game.add_member(request.user)

                        # return HttpResponse

                        return render(request, 'chatUI/chat.html', {'room': code, 'message': game.get_round_messages(),
                                                                    'round': game.current_round})
                    else:
                        return HttpResponse('room is full!')
                else:
                    return render(request, 'chatUI/chat.html', {'room': code, 'message': game.get_round_messages(),
                                                                'round': game.current_round})
                    print 'its here'
            except Game.DoesNotExist:
                return HttpResponse('Your url is not valid')
        else:
            return HttpResponse('Your url is not valid')
    else:
        return HttpResponse('Your request was not get')
