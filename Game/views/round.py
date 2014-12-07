from django.http.response import HttpResponse
from Game.models import Game

__author__ = 'Iman'


def end_round(request):
    print "end_round"
    room_code = request.POST['room']
    game = Game.objects.get(code=room_code)
    game.current_round.calculate_result_of_election()
    game.goto_next_round()
    return HttpResponse()
