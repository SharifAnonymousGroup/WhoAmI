import new
from django import forms
from Game.models import Game

__author__ = 'MiladDK'


class NewgameForm(forms.Form):
    time_of_each_round = forms.IntegerField()  # in second
    max_number_of_players = forms.IntegerField()
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Name'}))

