from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from Game.forms.newgame_form import NewgameForm
from Game.models import Game
from UserManagement.models import Member


__author__ = 'MiladDK'


@login_required
def newgame_request(request):
    if request.method == "POST":
        form = NewgameForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            name = cd['name']
            max_number_of_players = cd['max_number_of_players']
            time_of_each_round = cd['time_of_each_round']
            member = Member.objects.get(username=request.user.username)
            game = Game.objects.create_game(name=name, time_of_each_round=time_of_each_round,
                                            max_number_of_players=max_number_of_players, creator=member)
            game.add_member(request.user)
            return HttpResponseRedirect(game.get_url())
            #return HttpResponse('your room was created. your room link is ' + game.get_url())
    else:
        return HttpResponse("Your Request was not POST Method")
