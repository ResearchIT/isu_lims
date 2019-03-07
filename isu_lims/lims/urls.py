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
    path('thanks', views.thanks, name='thanks'),
    path('genus/<int:pk>/', GenusDetailView.as_view(), name='genus-detail'),
    path('subgenus/<int:pk>/', SubenusDetailView.as_view(), name='subgenus-detail'),
    path('genome/<int:pk>/', GenomeDetailView.as_view(), name='genome-detail'),
    path('species/<int:pk>/', SpeciesDetailView.as_view(), name='species-detail'),
    path('accession/<int:pk>/', AccessionDetailView.as_view(), name='accession-detail'),
    path('plant/<int:pk>/', PlantDetailView.as_view(), name='plant-detail'),
    path('seedpacket/<int:pk>/', SeedPacketDetailView.as_view(), name='seedpacket-detail'),
    path('seed/<int:pk>/', SeedDetailView.as_view(), name='seed-detail'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('sample/<int:pk>/', SampleDetailView.as_view(), name='sample-detail'),


]