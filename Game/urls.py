__author__ = 'Iman'
from django.conf.urls import patterns, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^newgame/$', 'Game.views.newgame.newgame', name='new_game'),
                       url(r'^newgame_request/$', 'Game.views.newgame.newgame_request',
                           name='new_game_request'),
                       url(r'^rooms/', 'Game.views.rooms.room', name='rooms')
)