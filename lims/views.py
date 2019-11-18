from django.shortcuts import render
from django_tables2 import SingleTableView
from django_tables2.views import SingleTableMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from . import models, tables

def index(request):
    return render(request, 'lims/index.html')

def thanks(request):
    return render(request, 'lims/thanks.html')

class AccessionTableView(PermissionRequiredMixin, SingleTableView):
    # django
    queryset = models.Accession.objects.select_related('species', 'species__genome', 'species__genome__subgenus', 'species__genome__subgenus__genus')
    template_name = "lims/filterable_overview_table_page.html"
    # django-tables2
    table_class = tables.AccessionTable
    # PermissionRequiredMixin
    permission_required = 'lims.view_accession'

class ProjectTableView(PermissionRequiredMixin, SingleTableView):
    # django
    model = models.Project
    template_name = "lims/filterable_overview_table_page.html"
    # django-tables2
    table_class = tables.ProjectTable
    # PermissionRequiredMixin
    permission_required = 'lims.view_project'

class PlantTableView(PermissionRequiredMixin, SingleTableView):
    # django
    model = models.Plant
    template_name = "lims/filterable_overview_table_page.html"
    # django-tables2
    table_class = tables.PlantTable
    # PermissionRequiredMixin
    permission_required = 'lims.view_plant'

class SeedPacketTableView(PermissionRequiredMixin, SingleTableView):
    # django
    model = models.SeedPacket
    template_name = "lims/filterable_overview_table_page.html"
    # django-tables2
    table_class = tables.SeedPacketTable
    # PermissionRequiredMixin
    permission_required = 'lims.view_seedpacket'

class SampleTableView(PermissionRequiredMixin, SingleTableView):
    # django
    model = models.Sample
    template_name = "lims/filterable_overview_table_page.html"
    # django-tables2
    table_class = tables.SampleTable
    # PermissionRequiredMixin
    permission_required = 'lims.view_sample'

class HerbariumTableView(PermissionRequiredMixin, SingleTableView):
    # django
    model = models.Herbarium
    template_name = "lims/filterable_overview_table_page.html"
    # django-tables2
    table_class = tables.HerbariumTable
    # PermissionRequiredMixin
    permission_required = 'lims.view_herbarium'