from django.shortcuts import render

from django.views.generic import ListView

from player.models import Skater


class ListSkaterView(ListView):

    model = Skater
    template_name = 'skater_list.html'
