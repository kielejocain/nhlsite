import json

from django.http import JsonResponse

from django.views.generic import ListView, DetailView

from player.models import Skater, SkaterStats, SkaterPredictions, Standings


class ListSkaterView(ListView):

    model = Skater
    template_name = 'player/skater_list.html'


class DetailSkaterView(DetailView):

    model = Skater
    template_name = 'player/skater_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailSkaterView, self).get_context_data(**kwargs)
        context['skater'] = Skater.objects.get(pk=self.kwargs['pk'])
        skater_pk = context['skater'].pk
        context['skaterstats'] = SkaterStats.objects.filter(nhl_num=skater_pk)
        context['skaterpredictions'] = SkaterPredictions.objects.filter(pk=self.kwargs['pk']).first()
        return context


def player_graph(request):
    pk = request.GET.get('pk')
    preds = SkaterPredictions.objects.filter(pk=pk).first()
    stats = SkaterStats.objects.get(nhl_num=pk, season=2015)
    if stats.team3:
        team = stats.team3
    elif stats.team2:
        team = stats.team2
    else:
        team = stats.team
    team = Standings.objects.get(team=team)
    sh_assists = stats.sh_points - stats.sh_goals
    pp_assists = stats.pp_points - stats.pp_goals
    data = [
            {
                'title':'Games Played',
                'subtitle':'',
                'ranges':[0,0,preds.games_played,82],
                'measures':[0,0,stats.games_played],
                'markers':[preds.games_played*team.games_played/82]
            },
            {
                'title':'Goals',
                'subtitle':'SH / ES / PP',
                'ranges':[preds.sh_goals,preds.sh_goals+preds.es_goals,preds.goals,60],
                'measures':[stats.sh_goals,stats.goals-stats.pp_goals,stats.goals],
                'markers':[preds.goals*team.games_played/82]
            },
            {
                'title':'Assists',
                'subtitle':'SH / ES / PP',
                'ranges':[preds.sh_assists,preds.sh_assists+preds.es_assists,preds.assists,80],
                'measures':[sh_assists,stats.assists-pp_assists,stats.assists],
                'markers':[preds.assists*team.games_played/82]
            },
            {
                'title':'Points',
                'subtitle':'SH / ES / PP',
                'ranges':[preds.sh_points,preds.sh_points+preds.es_points,preds.points,120],
                'measures':[stats.sh_points,stats.points-stats.pp_points,stats.points],
                'markers':[preds.points*team.games_played/82]
            },
            {
                'title':'Shots',
                'subtitle':'',
                'ranges':[0,0,preds.shots,500],
                'measures':[0,0,stats.shots],
                'markers':[preds.shots*team.games_played/82]
            },
            {
                'title':'TOI/Game',
                'subtitle':'SH / ES / PP',
                'ranges':[preds.sh_toi/(60*preds.games_played),(preds.sh_toi+preds.es_toi)/(60*preds.games_played),preds.toi/(60*preds.games_played),30],
                'measures':[stats.sh_toi/(60*stats.games_played),(stats.sh_toi+stats.es_toi)/(60*stats.games_played),stats.toi/(60*stats.games_played)],
                'markers':[preds.toi/(60*preds.games_played)]}
        ]
    return JsonResponse(data, safe=False)
