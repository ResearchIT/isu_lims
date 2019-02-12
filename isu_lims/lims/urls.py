from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('genus/', views.genus, name='genus'),
=======
    path('genera', views.genera, name='genera')
>>>>>>> 944f8154a76e213ba3966cd7d1afda05de34039e
]