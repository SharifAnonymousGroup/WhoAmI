from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render

from Game.models import Game, Player
from Game.views.election import election


__author__ = 'Iman'

@login_required
def ready_for_game(request):
    if request.method == 'POST':
        user = request.user
        player = Player.objects(member=user, isAlive=True)
        if not player.isReady:
            player.isReady = True
            player.game.number_of_ready_players += 1
            player.game.save()
            player.save()
            if player.game.number_of_ready_players == player.game.number_of_players:
                player.game.goto_next_round()

    else:
        HttpResponse('Your request is not post')


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
                    if game.number_of_players < game.max_number_of_players and not game.is_started:
                        game.add_member(request.user)
                        dic = {'room': game, 'message': game.get_round_messages(),
                               'round': game.current_round}
                        election_dic = election(request)
                        z = dict(dic.items() + election_dic.items())
                        return render(request, 'WhoAmI/game_page.html',  z)
                    else:
                        return HttpResponse('room is full!')
                else:
                    dic = {'room': game, 'message': game.get_round_messages(),
                           'round': game.current_round}
                    election_dic = election(request)
                    z = dict(dic.items() + election_dic.items())
                    return render(request, 'WhoAmI/game_page.html', z)

            except Game.DoesNotExist:
                return HttpResponse('Your url is not valid')
        else:
            return HttpResponse('Your url is not valid')
    else:
        return HttpResponse('Your request was not get')


