from django.http import HttpResponse
from django.template import loader

from .models import Genus

def index(request):
    return HttpResponse("Hello! Welcome to Wendel Lab Database.")

def genus(request):
    genera_list = Genus.objects
    template = loader.get_template('lims/index.html')
    context = {
        'genera_list': genera_list,
    }
    return HttpResponse(template.render(context, request))