from django.contrib.auth.decorators import login_required
from django.shortcuts import render

__author__ = 'garfild'


@login_required
def chat(request):
    return render(request, 'chatUI/chat.html', {})

