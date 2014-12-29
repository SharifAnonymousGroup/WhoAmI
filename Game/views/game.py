from django.shortcuts import render_to_response
from django.template import RequestContext

from Game.forms.newgame_form import NewgameForm
from Game.models import Game


__author__ = 'garfild'


def game(request):
    rooms = Game.objects.filter(is_active=True)
    print rooms
    form = NewgameForm()
    #return render(request, 'WhoAmI/main_page.html',{"form" : form})
    return render_to_response('WhoAmI/main_page.html',{"form" : form, "rooms" : rooms}, context_instance=RequestContext(request))