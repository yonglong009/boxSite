from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from .models import Question
# Create your views here.


def index(request):
    # template = loader.get_template('firstApp/index.html')
    # context = RequestContext(request, {})
    # return HttpResponse(template.render(context))
    context = {'first_name': 'Ma', 'last_name': 'Yonglong'}
    # return render(request, 'firstApp/index.html', context)
    return render_to_response('firstApp/index.html', context, context_instance=RequestContext(request))

