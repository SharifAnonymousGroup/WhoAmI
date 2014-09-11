from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from Game.forms.newgame_form import NewgameForm
from Game.models import Game

__author__ = 'MiladDK'
@login_required
def create_newgame(request):
    if request.method == "POST" :
        form = NewgameForm(request.POST)
        if form.is_valid():
            game = Game(form.name, form.time_of_each_round, form.max_number_of_player, request.user)
    else :
        HttpResponse("Your Request was not POST Method")
