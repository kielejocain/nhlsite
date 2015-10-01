from player.models import Player, SkaterStats
from django.template import RequestContext
from django.shortcuts import render_to_response

def search(request):
    query = request.GET.get('q')
    results = Player.objects.filter(last_name__icontains=query)
    context = RequestContext(request)
    return render_to_response('search/results.html', {"results": results,}, context_instance=context)