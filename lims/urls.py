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
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('admin/login/', RedirectView.as_view(pattern_name='oidc_authentication_init', query_string=True, permanent=False), name='login'),
    path('admin/default-login/', admin.site.login, name='default-admin-login'),
    path('admin/', admin.site.urls),
    path('admin/sample/import', views.ImportSamplesAdminView.as_view(), name='import_samples'),
    path('admin/seedpacket/import', views.ImportSeedpacketsAdminView.as_view(), name='import_seedpackets'),
    path('oidc/', include('mozilla_django_oidc.urls')),
    path('accession', views.AccessionTableView.as_view(), name='accession'),
    path('project', views.ProjectTableView.as_view(), name='project'),
    path('plant', views.PlantTableView.as_view(), name='plant'),
    path('seedpacket', views.SeedPacketTableView.as_view(), name='seedpacket'),
    path('sample', views.SampleTableView.as_view(), name='sample'),
    path('herbarium', views.HerbariumTableView.as_view(), name='herbarium'),
    path('', views.index, name='index'),
]
