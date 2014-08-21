from httplib import HTTPResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Chat/chat_test.html', {})

def send_message(request):
    return HTTPResponse('salam');
