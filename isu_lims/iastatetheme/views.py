from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import SiteTheme

def header(request):
    template = loader.get_template('iastatetheme/header.html')
    context = {
        'site_name': SiteTheme.objects.only('site_name'),
    }
    return HttpResponse(template.render(context, request))

def index(request):
    template = loader.get_template('watermetrics/index.html')
    context = {
        'site_name': SiteTheme.objects.only('site_name'),
    }
    return HttpResponse(template.render(context, request))
