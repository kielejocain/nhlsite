from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from home import views
import player.views
import search.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    # url(r'^polls/', include('polls.urls', namespace="polls")),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'home.views.index', name='home'),
    url(r'^search/$', search.views.search, name='search'),
    url(r'^player/$', player.views.ListSkaterView.as_view(),
        name="skater_list",
    ),
    url(r'^player/(?P<pk>\d{7})', player.views.DetailSkaterView.as_view(),
        name="player_detail"),
)

urlpatterns += staticfiles_urlpatterns()