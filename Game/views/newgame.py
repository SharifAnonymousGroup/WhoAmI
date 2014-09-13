from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from Game.forms.newgame_form import NewgameForm
from Game.models import Game

__author__ = 'MiladDK'
@login_required
def newgame(request):
    form = NewgameForm()
    return render(request, 'test/new_game_test.html', {'form': form})

@login_required
def newgame_request(request):
    if request.method == "POST" :
        form = NewgameForm(request.POST)
        if form.is_valid():
            game = Game(form.name, form.time_of_each_round, form.max_number_of_player, request.user)
    else :
        HttpResponse("Your Request was not POST Method")
