import os
import operator
from django.views.generic import ListView
from team.models import GoalieStats, PlayerTeam, SkaterStats
from itertools import chain


class DetailTeamView(ListView):

    model = SkaterStats
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
        query = PlayerTeam.objects.filter(
            season=os.environ['NHL_SEASON'],
            team=self.kwargs['team'],
            current=True
        ).select_related('nhl_num')
        forwards = []
        defensemen = []
        goalies = []
        for player in query:
            if player.nhl_num.player_position == 'D':
                defensemen += [player.nhl_num.nhl_num]
            elif player.nhl_num.player_position == 'G':
                goalies +=  [player.nhl_num.nhl_num]
            else:
                forwards += [player.nhl_num.nhl_num]
        forward_queries = [SkaterStats.objects.filter(season=os.environ['NHL_SEASON'], nhl_num=num) for num in forwards]
        context['forwards'] = chain(*forward_queries)
        context['forwards'] = sorted(context['forwards'], key=operator.attrgetter('nhl_num.last_name'))
        context['forwards'] = sorted(context['forwards'], key=operator.attrgetter('games_played'), reverse=True)
        context['forwards'] = sorted(context['forwards'], key=operator.attrgetter('points'), reverse=True)
        dman_queries = [SkaterStats.objects.filter(season=os.environ['NHL_SEASON'], nhl_num=num) for num in defensemen]
        context['defensemen'] = chain(*dman_queries)
        context['defensemen'] = sorted(context['defensemen'], key=operator.attrgetter('nhl_num.last_name'))
        context['defensemen'] = sorted(context['defensemen'], key=operator.attrgetter('games_played'), reverse=True)
        context['defensemen'] = sorted(context['defensemen'], key=operator.attrgetter('points'), reverse=True)
        goalie_queries = [GoalieStats.objects.filter(season=os.environ['NHL_SEASON'], nhl_num=num) for num in goalies]
        context['goalies'] = chain(*goalie_queries)
        context['goalies'] = sorted(context['goalies'], key=operator.attrgetter('nhl_num.last_name'))
        context['goalies'] = sorted(context['goalies'], key=operator.attrgetter('gaa'), reverse=True)
        context['goalies'] = sorted(context['goalies'], key=operator.attrgetter('games_started'), reverse=True)
        # query = SkaterStats.objects.filter(season=os.environ['NHL_SEASON'])
        # query1 = query.filter(team3=self.kwargs['team']).select_related('nhl_num')
        # query2 = query.filter(team3__isnull=True, team2=self.kwargs['team']).select_related('nhl_num')
        # query3 = query.filter(team3__isnull=True, team2__isnull=True, team=self.kwargs['team']).select_related('nhl_num')
        # context['skaters'] = chain(query1, query2, query3)
        # context['skaters'] = sorted(context['skaters'], key=operator.attrgetter('nhl_num.last_name'))
        # context['skaters'] = sorted(context['skaters'], key=operator.attrgetter('games_played'), reverse=True)
        # context['skaters'] = sorted(context['skaters'], key=operator.attrgetter('points'), reverse=True)
        return context