from django.shortcuts import render

__author__ = 'garfild'


def forget_password(request):
    return render(request,'test/forget_password_test.html',{})