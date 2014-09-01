from django.http.response import HttpResponse
from django.shortcuts import render

from UserManagement.forms.signup_form import *


__author__ = 'garfild'


def signup(request):
    form = SignupForm()
    return render(request, 'test/signup_test.html', {'form': form})


def signup_request(request):
    print 'salam'
    if request.method == 'POST':
        form = SignupForm(request.POST)
        print form.errors
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']
            first_name = cd['first_name']
            last_name = cd['last_name']
            gender = cd['gender']
            email = cd['email']
            age = cd['age']
            confirm_password = cd['confirm_password']
            if password == confirm_password:
                Member.objects.create_member(username=username, password=password, first_name=first_name,
                                             last_name=last_name, gender=gender, email=email, age=age)

        return HttpResponse()