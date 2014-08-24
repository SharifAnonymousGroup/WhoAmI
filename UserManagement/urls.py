from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login/$', 'UserManagement.views.login', name='login'),
    url(r'^login_request/' , 'UserManagement.views.login_request', name = 'login_request')

)