from datetime import timedelta
import json
import urllib
import random
import string

from django.core.mail.message import EmailMultiAlternatives
from django.template.context import Context
from django.template.loader import get_template
from django.utils import timezone
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from UserManagement.models import Member
from Utils.send_mail.asynchronous_send_mail import send_mail
from WhoAmI import settings


__author__ = 'garfild'
MAIL = "whoisme314@gmail.com"
SITE_NAME = "WHO AM I"


def forget_password(request):
    return render(request, 'test/forget_password_test.html', {'error': False})

@csrf_protect
@csrf_exempt
def forget_password_request(request):
    response_data = {}
    response_data['err'] = {}
    if request.method == 'POST':
        username_or_email = request.POST['username']
        if username_or_email == '':
            print "what is your name"
            response_data['err']['username_or_email'] = "this field is empty"
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        if '@' in username_or_email:
            kwargs = {'email': username_or_email}
        else:
            kwargs = {'username': username_or_email}

        try:
            user = Member.objects.get(**kwargs)
            random_code = generate_code()
            user.reset_password_code = random_code
            user.reset_password_expiredtime = timezone.now() + timedelta(hours=4)
            print user.reset_password_expiredtime
            user.save()
            params = urllib.urlencode({
                "code": random_code,
                "user": user.username,
                })
            url = settings.SITE_URL + "/account/reset_password/?" + params
            send_mail('reset your password', MAIL, [user.email],
                      'email_test/reset_password_mail.txt',
                      'email_test/reset_password_mail.html',
                      {'username': user.username, 'url': url})
            response_data['err']['status'] = 'email send to your email'
            return HttpResponse(json.dumps(response_data), content_type="application/json")
            # return HttpResponse('reset password mail was sent to your mail!')
        except Member.DoesNotExist:
            response_data['err']['status'] = 'invalid username or email'
            return HttpResponse(json.dumps(response_data), content_type="application/json")
            # return render(request, 'test/forget_password_test.html', {'error': True})

    else:
        response_data['err']['request_method'] = "Your method is not post"
        return HttpResponse(json.dumps(response_data), content_type="application/json")
        # return HttpResponse("Your request is not POST")


def generate_code():
    chars = string.ascii_letters + string.digits
    size = 30
    return ''.join(random.choice(chars) for _ in range(size))


