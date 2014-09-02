from django.core.mail import send_mail

from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from UserManagement.forms.signup_form import *


__author__ = 'garfild'

MAIL = "whoisme314@gmail.com"
SITE_NAME = "WHO AM I"


@csrf_protect
@csrf_exempt
def signup(request):
    form = SignupForm()
    return render(request, 'test/signup_test.html', {'form': form})


@csrf_protect
@csrf_exempt
def signup_request(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']
            first_name = cd['first_name']
            last_name = cd['last_name']
            gender = cd['gender']
            email = cd['email']
            age = cd['age']
            Member.objects.create_member(username=username, password=password, first_name=first_name,
                                         last_name=last_name, gender=gender, email=email, age=age)
            signup_mail(first_name, email)
        else:
            return render(request, 'test/signup_test.html', {'form': form})

    return HttpResponse()


def signup_mail(name, email):
    subject = "Welcome to Who Am I!"
    message = "Hi " + name + "!\n" + "I glad to have good time with Who Am I."
    send_mail(subject, message, MAIL,
              [email], fail_silently=False)
    pass