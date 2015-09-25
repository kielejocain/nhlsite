from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import home.views
import player.views
import search.views
import stats.views
import about.views
import team.views

urlpatterns = patterns(
    '',
    url(r'^$', home.views.index, name='home'),
    url(r'^search/$', search.views.search, name='search'),
    url(r'^player/$', player.views.ListSkaterView.as_view(),
        name="skater_list",
        ),
    url(r'^player/(?P<pk>\d{7})', player.views.DetailSkaterView.as_view(),
        name="player_detail"
        ),
    url(r'^stat/glossary', stats.views.glossary, name="glossary"),
    url(r'^about/site', about.views.site, name="site"),
    url(r'^about/method', about.views.method, name="method"),
    url(r'^stat/goals', stats.views.goals, name="goal_detail"),
    url(r'^team/(?P<team>\w{3})', team.views.DetailTeamView.as_view(), name="team_detail"),
    url(r'^api/player_graph/$', player.views.player_graph, name="player_graph")
    )

urlpatterns += staticfiles_urlpatterns()
