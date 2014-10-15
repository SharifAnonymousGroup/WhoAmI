from django.shortcuts import render
from Game.models import Game


__author__ = 'garfild'


def game(request):
    return render(request, 'WhoAmI/main_page.html',{})