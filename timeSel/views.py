from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

def render_template(request, params, path):
    template = loader.get_template('timeSel\\' + path)
    context = RequestContext(request, params)
    return HttpResponse(template.render(context))

def index(request):
    return render_template(request, {}, 'index.html')