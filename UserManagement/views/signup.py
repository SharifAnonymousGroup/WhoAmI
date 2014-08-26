from django.http.response import HttpResponse

from django.shortcuts import render

from UserManagement.models import Member


__author__ = 'garfild'


def signup(request):
    return render(request, 'test/signup_test.html')


def signup_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        gender = request.POST['gender']
        email = request.POST['email']
        age = request.POST['age']
        member = Member.objects.create_member(username=username, password=password, first_name=first_name,
                                              last_name=last_name, gender=gender, email=email, age=age)
        print "good"
        return HttpResponse()