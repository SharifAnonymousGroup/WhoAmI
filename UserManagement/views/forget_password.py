from django.shortcuts import render
from UserManagement.models import Member

__author__ = 'garfild'


def forget_password(request):
    return render(request, 'test/forget_password_test.html', {})


def forget_password_request(request):
    username = ''
    if request.method == 'POST':
        username_or_email = request.POST['username']
        if '@' in username_or_email:
            user = Member.objects.get(gmail=username_or_email)
        else:
            user = Member.objects.get(username=username_or_email)
