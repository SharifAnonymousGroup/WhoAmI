from django.conf.urls import patterns, include, url

from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WhoAmI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'UserManagement.views.main.main_page', name='main'),
    url(r'^account/', include('UserManagement.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^game/', include('Game.urls')),
)
