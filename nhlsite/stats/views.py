from django.shortcuts import render_to_response
from django.template import RequestContext

def goals(request):
    return render_to_response('stats/goals.html', context_instance=RequestContext(request))