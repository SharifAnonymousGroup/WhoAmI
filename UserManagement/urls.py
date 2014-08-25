from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout

from django.contrib import admin
import UserManagement

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login/$', 'UserManagement.login.login', name='login'),
    url(r'^login_request/' , 'UserManagement.login.login_request', name = 'login_request'),
    url(r'^signup/$', 'UserManagement.signup.signup', name='signup'),
    url(r'^signup_request/$','UserManagement.signup.signup_request',name='signup_request'),


)