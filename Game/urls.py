from kombu.utils import url
from Game.models import Game

__author__ = 'Iman'
from django.conf.urls import patterns, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

                       url(r'^$', 'Game.views.game.game', name='game'),

                       url(r'^leavegame/$', 'Game.views.chat.leave_game'),

                       url(r'^chat/send_message/$', 'Game.views.chat.send_message', name='send_message'),

                       url(r'^newgame_request/$', 'Game.views.newgame.newgame_request',
                           name='new_game_request'),
                       url(r'^rooms/', 'Game.views.rooms.room', name='rooms'),
                       url(r'^election/', 'Game.views.election.election', name='election'),
                       url(r'^election_request/', 'Game.views.election.election_request', name='election_request'),

                       url(r'^endgame/$', 'Game.views.endgame.end', name='end_game'),

                       url(r'^chat/$', 'Game.views.chat.chat'),
                       url(r'^end_round/$', 'Game.views.round.end_round'),
                       url(r'^ready_for_game/$', 'Game.views.rooms.ready_for_game')

)
