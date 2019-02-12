from django.urls import path

from . import views

urlpatterns = [
    path('', views.header, name='header'),
    path('', views.index, name='index')
]
