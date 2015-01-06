from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import player.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nhlsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^player/$', player.views.ListSkaterView.as_view(),
        name="skater_list",
    ),
    url(r'^player/(?P<pk>\d{7})', player.views.DetailSkaterView.as_view(),
        name="player_detail"),
)

urlpatterns += staticfiles_urlpatterns()