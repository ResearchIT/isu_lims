from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('genera', views.genera, name='genera')
]