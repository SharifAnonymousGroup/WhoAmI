import new
from django import forms
from Game.models import Game

__author__ = 'MiladDK'


class NewgameForm(forms.Form):
    time_of_each_round = forms.IntegerField(max_value=300)  # in second
    max_number_of_players = forms.IntegerField(max_value=12)
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))

