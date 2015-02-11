from django.shortcuts import render

from django.views.generic import ListView

from team.models import CurrSkaterStats

from itertools import chain

import operator


class DetailTeamView(ListView):

    model = CurrSkaterStats
    template_name = 'team/team_detail.html'

    def get_context_data(self, **kwargs):
        NAMES = {"ANA": "Anaheim Ducks",
             "ARI": "Arizona Coyotes",
             "BOS": "Boston Bruins",
             "BUF": "Buffalo Sabres",
             "CGY": "Calgary Flames",
             "CAR": "Carolina Hurricanes",
             "CHI": "Chicago Blackhawks",
             "COL": "Colorado Avalanche",
             "CBJ": "Columbus Blue Jackets",
             "DAL": "Dallas Stars",
             "DET": "Detroit Red Wings",
             "EDM": "Edmonton Oilers",
             "FLA": "Florida Panthers",
             "LAK": "Los Angeles Kings",
             "MIN": "Minnesota Wild",
             "MTL": "Montreal Canadiens",
             "NSH": "Nashville Predators",
             "NJD": "New Jersey Devils",
             "NYI": "New York Islanders",
             "NYR": "New York Rangers",
             "OTT": "Ottawa Senators",
             "PHI": "Philadelphia Flyers",
             "PIT": "Pittsburgh Penguins",
             "SJS": "San Jose Sharks",
             "STL": "St. Louis Blues",
             "TBL": "Tampa Bay Lightning",
             "TOR": "Toronto Maple Leafs",
             "VAN": "Vancouver Canucks",
             "WSH": "Washington Capitals",
             "WPG": "Winnipeg Jets"
             }
        context = super(DetailTeamView, self).get_context_data(**kwargs)
        context['team'] = self.kwargs['team']
        context['full_team'] = NAMES[context['team']]
        query1 = CurrSkaterStats.objects.filter(team3=self.kwargs['team']).select_related('nhl_num')
        query2 = CurrSkaterStats.objects.filter(team3__isnull=True, team2=self.kwargs['team']).select_related('nhl_num')
        query3 = CurrSkaterStats.objects.filter(team3__isnull=True, team2__isnull=True, team=self.kwargs['team']).select_related('nhl_num')
        context['skaters'] = chain(query1, query2, query3)
        context['skaters'] = sorted(context['skaters'], key=operator.attrgetter('nhl_num.last_name'))
        context['skaters'] = sorted(context['skaters'], key=operator.attrgetter('games_played'), reverse=True)
        context['skaters'] = sorted(context['skaters'], key=operator.attrgetter('points'), reverse=True)
        return context