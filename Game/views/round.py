from django.http.response import HttpResponse

from Game.models import Game


__author__ = 'Iman'


def end_round(request):
    print "agha man seda shodam chaghal dayoos"
    room_code = request.GET['room']
    print room_code
    game = Game.objects.get(code=room_code)
    game.current_round.calculate_result_of_election()
    print game.current_round.turn
    game.goto_next_round()
    return HttpResponse("javabe endgame django be node")
