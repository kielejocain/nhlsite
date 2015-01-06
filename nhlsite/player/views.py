from django.shortcuts import render

from django.views.generic import ListView, DetailView

from player.models import Skater, Skaterstats, SkaterPredictions


class ListSkaterView(ListView):

    model = Skater
    template_name = 'skater_list.html'

class DetailSkaterView(DetailView):

    model = Skater
    template_name = 'skater_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailSkaterView, self).get_context_data(**kwargs)
        context['skater'] = Skater.objects.get(pk=self.kwargs['pk'])
        skater_pk = context['skater'].pk
        context['skaterstats'] = Skaterstats.objects.filter(nhl_num=skater_pk)
        context['skaterpredictions'] = SkaterPredictions.objects.get(pk=self.kwargs['pk'])
        return context
