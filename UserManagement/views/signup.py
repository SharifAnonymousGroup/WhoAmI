import json

from django.http.response import HttpResponse

from django.shortcuts import render
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
            print "zakhar"
        else:
            form.cleaned_data['password'] = ""
            form.cleaned_data['confirm_password'] = ""

            # response = form.errors_as_json(strip_tags=True)
            # print response
            # return render(request, 'UserManagementUI/homepage.html', {'form': form, 'login_error': False,
            # 'forget_password_error': False})
            print "not zakhar"
            response_data = {'err': form.errors}
            return HttpResponse(json.dumps(response_data), content_type="application/json")

        return render(request, 'test/login_test.html', {})
    else:
        return HttpResponse('Your request method was not POST')


