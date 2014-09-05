from django.contrib import auth
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from UserManagement.models import Member


def login(request):
    return render(request, 'test/login_test.html', {})


def login_request(request):
    if request.method == 'POST':
        username_or_email = request.POST['username']  # it might be email so we check if the entry is email or username

        if '@' in username_or_email:
            kwargs = {'email': username_or_email}
        else:
            kwargs = {'username': username_or_email}

        try:
            user = Member.objects.get(**kwargs)
        except Member.DoesNotExist:
            return render(request, 'test/login_test.html', {'error': True})

        password = request.POST['password']
        username = user.username
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            print "login was successful by " + user.username
            return HttpResponse('You successfully loged in as ' + user.username)
        else:
            print "password was not correct"
            return render(request, 'test/login_test.html', {'error': True})
    else:
        return HttpResponse('Your request method was not POST')

