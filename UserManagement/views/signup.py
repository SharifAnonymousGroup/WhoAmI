from django.core.mail.message import EmailMultiAlternatives
from django.http.response import HttpResponse
from django.template import Context

from django.shortcuts import render

from django.template.loader import get_template
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from UserManagement.forms.signup_form import *
from Utils.send_mail.asynchronous_send_mail import send_mail


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

            send_mail('Welcome to Who Am I', MAIL, [email],
                      'email_test/registration_mail.txt',
                      'email_test/registration_mail.html',
                      {'username': username})
        else:
            form.cleaned_data['password'] = ""
            form.cleaned_data['confirm_password'] = ""
            return render(request, 'test/signup_test.html', {'form': form})
        return HttpResponse('You registered successfully')
    else:
        return HttpResponse('Your request method was not POST')


