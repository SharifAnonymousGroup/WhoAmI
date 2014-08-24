from django.contrib import auth
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'test/login_test.html', {})


def login_request(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        print "correct"
    else:
        print "not correct"
        return render(request, 'test/login_test.html', {'error': True})
    return HttpResponse()