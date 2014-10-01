from logging import PlaceHolder
from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import CheckboxInput

from UserManagement.models import Member, GENDER_CHOISES


class SignupForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'UserName'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    age = forms.IntegerField(max_value=100, widget=forms.TextInput(attrs={'placeholder': 'Age'}), required=False)
    gender = forms.ChoiceField(choices=GENDER_CHOISES)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

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

    # def clean_password(self):
    #     password = self.cleaned_data['password']
    #     print "password is : "  + password
    #     if  self.cleaned_data['password'] is None:
    #         raise ValidationError("Password is empty")

    def clean(self):
        cd = self.cleaned_data
        password = cd.get('password', '')
        confirm_password = cd.get('confirm_password', '')
        if password != confirm_password:
            self._errors['password'] = self.error_class(["Your Passwords don't match"])
        return cd

    class Meta:
        model = Member
        field = (
            'first_name', 'last_name', 'username', 'email', 'age', 'gender', 'password', 'confirm_password',
            'term_accept')

