from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'Chat/chat_test.html', {})


def message_handler(request):
    user = request.user;
    message = request.GET.get('message');
    return HttpResponse()
