from datetime import timedelta
import urllib
from django.contrib.sites.models import Site
from django.core.mail.message import EmailMultiAlternatives
from django.template.context import Context
from django.template.loader import get_template
from django.utils import timezone
import random
import string
from django.http.response import HttpResponse
from django.shortcuts import render
from UserManagement.models import Member
from WhoAmI import settings

__author__ = 'garfild'
MAIL = "whoisme314@gmail.com"
SITE_NAME = "WHO AM I"


def forget_password(request):
    return render(request, 'test/forget_password_test.html', {'error': False})


def forget_password_request(request):
    if request.method == 'POST':
        username_or_email = request.POST['username']
        if '@' in username_or_email:
            kwargs = {'email': username_or_email}
        else:
            kwargs = {'username': username_or_email}

        try:
            user = Member.objects.get(**kwargs)
            random_code = generate_code()
            user.reset_password_code = random_code
            user.reset_password_expiredtime = timezone.now() + timedelta(hours=4)
            user.save()
            params = urllib.urlencode({
                "code": random_code,
                "user": user.username,
            })
            url = settings.SITE_URL + "/account/reset_password/?" + params
            reset_password_mail(user.username, url, user.email)
        except Member.DoesNotExist:
            return render(request, 'test/forget_password_test.html', {'error': True})

        return HttpResponse("Your password reset send to your mail")

    else:
        return HttpResponse("Your request is not POST")

def generate_code():
    chars = string.ascii_letters + string.digits
    size = 30
    return ''.join(random.choice(chars) for _ in range(size))

def reset_password_mail(username, url, email):
    plaintext = get_template('email_test/reset_password_mail.txt')
    html = get_template('email_test/reset_password_mail.html')
    d = Context({'username': username, 'url': url})
    subject, from_email, to = 'reset your password', MAIL, email
    text_content = plaintext.render(d)
    html_content = html.render(d)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    print 'mail was sent!'
