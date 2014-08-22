from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WhoAmI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'Chat.views.home', name='home'),
    url(r'^message_handler' , 'Chat.views.message_handler', name='message_handler'),

)