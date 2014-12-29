from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render

from Game.models import Game, Player


__author__ = 'Iman'


@login_required
def ready_for_game(request):
    if request.method == 'GET':
        user = request.user
        player = Player.objects.get(member=user, isAlive=True)
        print player
        print player.game.max_number_of_players
        print player.game.number_of_ready_players
        player_is_ready = player.isReady
        if not player.isReady:
            player.isReady = True
            player.game.number_of_ready_players += 1
            player.game.save()
            player.save()
        if player.game.number_of_ready_players == player.game.max_number_of_players and not player_is_ready:
            player.game.goto_next_round()
        return HttpResponse("it's ok")

    else:
        return HttpResponse('Your request is not post')


@login_required
def room(request):
    user = request.user
    if request.method == 'GET':
        code = request.GET.get('code', '')
        if code != '':
            try:
                game = Game.objects.get(code=code)
                if not game.is_active:
                    return HttpResponse('your link is expired')
                if not game.have_member(user):
                    if game.number_of_players < game.max_number_of_players and not game.is_started:
                        game.add_member(user)
                        dic = {'room': game, 'message': game.get_round_messages(),
                               'round': game.current_round}
                        election_dic = get_election_information(user)
                        z = dict(dic.items() + election_dic.items())
                        return render(request, 'WhoAmI/game_page.html', z)
                    else:
                        return HttpResponse('room is full!')
                else:
                    dic = {'room': game, 'message': game.get_round_messages(),
                           'round': game.current_round}
                    print "zakhare asli iman "
                    election_dic = get_election_information(user)
                    print "zakhare badi"
                    z = dict(dic.items() + election_dic.items())
                    return render(request, 'WhoAmI/game_page.html', z)

            except Game.DoesNotExist:
                return HttpResponse('Your url is not valid')
        else:
            return HttpResponse('Your url is not valid')
    else:
        return HttpResponse('Your request was not get')



def get_election_information(user):

    # player = user.current_player
    print "ghabl"
    player = Player.objects.get(member=user, isAlive=True)
    print "ba'd"
    if player is None:
        return HttpResponse("you was not in this room")
    game = player.game

    players = Player.objects.filter(game=game, isAlive=True)
    colors = [eval(player.color)[1] for player in players]
    players = [player for player in players]
    # json_players = json.dumps(players)
    # dic = {'colors': colors, 'json_players': json_players, 'players': players}
    dic = {'colors': colors, 'players': players}
    # print players
    return dic
