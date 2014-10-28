from django import forms
from django.forms.formsets import formset_factory

__author__ = 'garfild'


class ElectionForm(forms.Form):
    voted = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': ''}))



