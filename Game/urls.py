__author__ = 'Iman'
from django.conf.urls import patterns, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^newgame$', 'Game.views.newgame', name='new_game'),
)