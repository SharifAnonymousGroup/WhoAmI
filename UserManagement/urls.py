from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout

from django.contrib import admin
import UserManagement

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login/$', 'UserManagement.views.login.login', name='login'),
    url(r'^login_request/' , 'UserManagement.views.login.login_request', name = 'login_request'),
    url(r'^signup/$', 'UserManagement.views.signup.signup', name='signup'),
    url(r'^signup_request/$', 'UserManagement.views.signup.signup_request',name='signup_request'),


)