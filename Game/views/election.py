import json

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse

from Game.models import Player, Vote
from UserManagement.models import Member


__author__ = 'garfild'


@login_required
def election(request):
    user = request.user

    # player = user.current_player
    player = Player.objects.get(member=user, isAlive=True)
    if player is None:
        return HttpResponse("you was not in this room")
    game = player.game

    players = Player.objects.filter(game=game, isAlive=True)
    colors = [eval(player.color)[1] for player in players]
    players = [player.member.username for player in players]
    json_players = json.dumps(players)
    dic = {'colors': colors, 'json_players': json_players, 'players': players}
    # print players
    return dic


@login_required()
def election_request(request):
    print "election"
    election_form = request.POST  # get bayad beshe post['election_form]      election form behesh color midi mige ke voted ki boode :)))
    if request.method == 'POST':  # not bayad bardashte she
        user = request.user
        player = Player.objects.get(member=user, isAlive=True)
        game = player.game
        players = Player.objects.filter(game=game, isAlive=True)
        colors = [eval(player.color)[1] for player in players]
        for color in colors:
            try:
                election_form[color]
            except:
                response = {'is_success': False,
                            'message': "You cheat because you change the color.your score is minez " + unicode(
                                len(players))}
                player.score -= len(players)
                return HttpResponse(json.dumps(response), content_type="application/json")
        target_list = []
        for color in colors:
            try:
                member = Member.objects.get(username=election_form[color])
                target_player = Player.objects.get(member=member, isAlive=True)
                if target_player.game != game:
                    response = {'is_success': False,
                                'message': election_form[color] + " not exists in this room!What the Fuck!"}
                    return HttpResponse(json.dumps(response), content_type="application/json")
                try:
                    vote = Vote.objects.get(round=game.current_round, voter=player, color=color)
                    print "hastesh"
                    vote.target = target_player
                    vote.save()
                except:
                    Vote.objects.create_vote(round=game.current_round, voter=player, color=color, target=target_player)
                    print "nistesh"


                # TODO bayad to model ha vote (voter,round) ro yekta konim ke felan balad nistam :))))))))
                if eval(player.color)[1] == color:
                    print "zakhar"
                    target_player.score -= 1
                    player.score += 1
                    target_player.save()
                    player.save()
            except:
                continue

    response = {'is_success': True, 'message': "your election was sucessful please wait for your friends!"}
    return HttpResponse(json.dumps(response), content_type="application/json")