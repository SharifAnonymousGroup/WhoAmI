from django.contrib import auth
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from UserManagement.models import Member


def login(request):
    return render(request, 'test/login_test.html', {})


def login_request(request):
    username_or_email = request.POST['username'] # it might be email so we check if the entry is email or username
    username = ''
    if '@' in username_or_email:
        user = Member.objects.get(email=username_or_email)
        if user is not None:
            username = user.username
    else:
        username = username_or_email
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        print "login was successful by " + user.username
    else:
        print "not correct"
        return render(request, 'test/login_test.html', {'error': True})
    return HttpResponse()

