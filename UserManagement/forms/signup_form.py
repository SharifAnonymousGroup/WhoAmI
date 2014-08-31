from django import forms
from django.forms.widgets import CheckboxInput

from UserManagement.models import Member, GENDER_CHOISES


class SignupForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    age = forms.IntegerField(max_value=100)
    gender = forms.ChoiceField(choices=GENDER_CHOISES)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    term_accept = forms.BooleanField(widget=CheckboxInput())

    class Meta:
        model = Member
        field = (
            'first_name', 'last_name', 'username', 'email', 'age', 'gender', 'password', 'confirm_password',
            'term_accept')

