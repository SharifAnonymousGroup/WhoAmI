from django.http.response import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from UserManagement.models import Member


def reset_password(request):
    if request.method == 'GET':
        code = request.GET.get('code', '')
        username = request.GET.get('user', '')

        try:
            user = Member.objects.get(username=username)
            if user.reset_password_code == code:
                if user.reset_password_expired():
                    return HttpResponse("Your link to reset your password is "
                                        "expired please request for new link in forget password page")
                else:
                    return render(request, 'test/reset_password_test.html',
                                  {'username': username, 'code': code, 'error': False})

            else:
                return HttpResponse("Your link to reset your password is not valid")
        except Member.DoesNotExist:
            return HttpResponse("Your link to reset your password is not valid")

    return HttpResponse("Your reqeust was not GET!")


def reset_password_request(request):
    if request.method == 'POST':
        code = request.POST['code']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        try:
            user = Member.objects.get(username=username)
            if code == user.reset_password_code:
                if user.reset_password_expired():
                    return HttpResponse("Your link to reset your password is "
                                        "expired please request for new link in forget password page")
                if password == confirm_password:
                    user.set_password(password)
                    user.save()
                    return HttpResponse("Your password successfully changed")
                else:
                    return render(request, 'test/reset_password_test.html',
                           {'username': username, 'code': code, 'error': True})
            else:
                return HttpResponse("Your request is not valid")
        except Member.DoesNotExist:
            return HttpResponse("Your request is not valid")
    else:
        return HttpResponse("Your request was not POST")
