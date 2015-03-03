from django.shortcuts import render_to_response
from django.template import RequestContext

def glossary(request):
    return render_to_response('stats/glossary.html', context_instance=RequestContext(request))

def method(request):
    return render_to_response('stats/method.html', context_instance=RequestContext(request))

def goals(request):
    return render_to_response('stats/goals.html', context_instance=RequestContext(request))