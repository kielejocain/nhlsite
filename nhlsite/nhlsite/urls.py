from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from home import views
import player.views
import search.views
import stats.views
import team.views

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
    url(r'^stat/glossary|Glossary', stats.views.glossary, name="glossary"),
    url(r'^stat/method|Method', stats.views.method, name="method"),
    url(r'^stat/goals|Goals', stats.views.goals, name="goal_detail"),
    url(r'^team/(?P<team>\w{3})', team.views.DetailTeamView.as_view(), name="team_detail"),
)

urlpatterns += staticfiles_urlpatterns()