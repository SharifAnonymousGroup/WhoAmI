from django.http.response import HttpResponse
from Game.models import Game
from UserManagement.models import Member

__author__ = 'Iman'

def room(request):
    if request.method == 'GET':
        code = request.GET.get('code', '')
        if code != '':
            try:
                game = Game.objects.get(code=code)
                if not game.have_member(Member(request.user)):
                    game.add_member(Member(request.user))
                #TODO
                #render(game)
            except Game.DoesNotExist:
                HttpResponse('Your url is not valid')
        else:
            HttpResponse('Your url is not valid')
    else:
        return HttpResponse('Your request was not get')