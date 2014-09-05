from django import forms
from django.core.exceptions import ValidationError
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

    def clean_username(self):
        username = self.cleaned_data["username"]
        if Member.objects.filter(username=username).exists():
            raise ValidationError("username already exists.")
        if "@" in username:
            raise ValidationError("username can't contain '@' character")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if Member.objects.filter(email=email).exists():
            raise ValidationError("email already exists.")
        return email

    def clean(self):
        cd = self.cleaned_data
        if cd['password'] != cd['confirm_password']:
            self._errors['password'] = "passwords don't match"
        return cd


    class Meta:
        model = Member
        field = (
            'first_name', 'last_name', 'username', 'email', 'age', 'gender', 'password', 'confirm_password',
            'term_accept')

