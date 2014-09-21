import json

from django.contrib import auth
from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from UserManagement.models import Member


def login(request):
    return render(request, 'test/login_test.html', {})


@csrf_protect
@csrf_exempt
def login_request(request):
    response_data = {}
    response_data['message'] = {}
    response_data['is_successful'] = False
    if request.method == 'POST':
        username_or_email = request.POST['username']  # it might be email so we check if the entry is email or username
        password = request.POST['password']
        if username_or_email == '':
            response_data['message']["username_or_email"] = "please enter your username or email"
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        if password == '':
            response_data['message']['password'] = "please enter your password"
            return HttpResponse(json.dumps(response_data), content_type="application/json")

        if '@' in username_or_email:
            kwargs = {'email': username_or_email}
        else:
            kwargs = {'username': username_or_email}

        try:
            user = Member.objects.get(**kwargs)
            password = request.POST['password']
            username = user.username
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.logout(request)
                auth.login(request, user)
                response_data['is_successful'] = True
                response_data['message'] = 'You successfully loged in as ' + user.username
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                # return render(request, 'test/login_test.html', {'error': True}
                response_data['message']['authentication failed'] = "username or password is wrong"
                return HttpResponse(json.dumps(response_data), content_type="application/json")
        except Member.DoesNotExist:
            response_data['message']['authentication failed'] = "username or password is wrong"
            return HttpResponse(json.dumps(response_data), content_type="application/json")




    else:
        response_data['err']['request_method'] = "Your request is not POST"
        return HttpResponse(json.dumps(response_data), content_type="application/json")

