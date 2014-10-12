from django.forms.formsets import formset_factory
from django.shortcuts import render
from Game.forms.election import ElectionForm
from Game.models import Player

__author__ = 'garfild'


def election(request):
    user = request.user
    player = Player.objects.get(member=user, isAlive=True)
    game = player.game
    players = Player.objects.filter(game=game)
    colors = [eval(player.color)[1] for player in players]

    return render(request, 'election/election.html', {'colors':colors})