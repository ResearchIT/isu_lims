"""lims URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('_nested_admin/', include('nested_admin.urls')),
    path('genera', views.GeneraTableView.as_view(), name='genera'),
    path('subgenera', views.SubGeneraTableView.as_view(), name='subgenera'),
    path('genome', views.GenomeTableView.as_view(), name='genome'),
    path('species', views.SpeciesTableView.as_view(), name='species'),
    path('accession', views.AccessionTableView.as_view(), name='accession'),
    path('project', views.ProjectTableView.as_view(), name='project'),
    path('plant', views.PlantTableView.as_view(), name='plant'),
    path('seedpacket', views.SeedPacketTableView.as_view(), name='seedpacket'),
    path('sample', views.SampleTableView.as_view(), name='sample'),
    path('herbarium', views.HerbariumTableView.as_view(), name='herbarium'),
    path('', views.index, name='index'),
]
