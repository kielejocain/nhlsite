from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.



def method(request):
    return render_to_response('about/method.html', context_instance=RequestContext(request))

def site(request):
    return render_to_response('about/site.html', context_instance=RequestContext(request))

def author(request):
    return render_to_response('about/author.html', context_instance=RequestContext(request))