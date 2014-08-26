from argparse import _ChoicesPseudoAction
from django import forms
from UserManagement.models import GENDER_CHOISES, Member


class SignupForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    age = forms.IntegerField(max_value=100)
    gender = forms.CharField(max_length=1, choices=GENDER_CHOISES, widget=forms.ChoiceField)
    password = forms.PasswordInput(widget=forms.PasswordInput)
    confirm_password = forms.PasswordInput(widget=forms.PasswordInput)