from django.http import HttpResponse
<<<<<<< HEAD
from django.template import loader
=======
from django.shortcuts import render
from iastatetheme.models import SiteTheme

from .models import Genus
>>>>>>> 944f8154a76e213ba3966cd7d1afda05de34039e

from .models import Genus

def index(request):
<<<<<<< HEAD
    return HttpResponse("Hello! Welcome to Wendel Lab Database.")

def genus(request):
    genera_list = Genus.objects
    template = loader.get_template('lims/index.html')
    context = {
        'genera_list': genera_list,
    }
    return HttpResponse(template.render(context, request))
=======
    return render(request, 'lims/index.html')

def genera(request):
    genera_list = Genus.objects.all()
    context = {'genera_list': genera_list,
    }

    return render(request, 'genera/index.html', context)

>>>>>>> 944f8154a76e213ba3966cd7d1afda05de34039e
