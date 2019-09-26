from django.shortcuts import render

def index(request):
    return render(request, 'lims/index.html')

def thanks(request):
    return render(request, 'lims/thanks.html')