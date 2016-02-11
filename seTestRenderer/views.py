from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.


def StateList(request):
    context = None

    return render_to_response('renderer/states.html',
                              context,
                              context_instance=RequestContext(request))
