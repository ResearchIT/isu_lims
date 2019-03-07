from django.urls import path
from . import views
from .views import GenusDetailView


urlpatterns = [
    path('', views.index, name='index'),
    path('genera', views.genera, name='genera'),
    path('subgenera', views.subgenera, name='subgenera'),
    path('genome', views.genome, name='genome'),
    path('species', views.species, name='species'),
    path('accession', views.accession, name='accession'),
    path('plant', views.plant, name='plant'),
    path('seedpacket', views.seedpacket, name='seedpacket'),
    path('seed', views.seed, name='seed'),
    path('project', views.project, name='project'),
    path('sample', views.sample, name='sample'),
    path('name', views.name, name='name'),
    path('thanks', views.thanks, name='thanks')
    path('genus/<int:pk>/', GenusDetailView.as_view(), name='genus-detail'),
]