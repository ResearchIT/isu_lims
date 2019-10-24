from django.shortcuts import render
from django_tables2 import SingleTableView
from django_tables2.views import SingleTableMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from . import models, tables

def index(request):
    return render(request, 'lims/index.html')

def thanks(request):
    return render(request, 'lims/thanks.html')

class GeneraTableView(PermissionRequiredMixin, SingleTableView):
    # django
    model = models.Genus
    template_name = "lims/filterable_overview_table_page.html"
    # django-tables2
    table_class = tables.GeneraTable
    # PermissionRequiredMixin
    permission_required = 'lims.view_genus'

class SubGeneraTableView(PermissionRequiredMixin, SingleTableView):
    # django
    model = models.Subgenus
    template_name = "lims/filterable_overview_table_page.html"
    # django-tables2
    table_class = tables.SubGeneraTable
    # PermissionRequiredMixin
    permission_required = 'lims.view_subgenus'

class GenomeTableView(PermissionRequiredMixin, SingleTableView):
    # django
    model = models.Genome
    template_name = "lims/filterable_overview_table_page.html"
    # django-tables2
    table_class = tables.GenomeTable
    # PermissionRequiredMixin
    permission_required = 'lims.view_genome'

class SpeciesTableView(PermissionRequiredMixin, SingleTableView):
    # django
    model = models.Species
    template_name = "lims/filterable_overview_table_page.html"
    # django-tables2
    table_class = tables.SpeciesTable
    # PermissionRequiredMixin
    permission_required = 'lims.view_species'

class AccessionTableView(PermissionRequiredMixin, SingleTableView):
    # django
    model = models.Accession
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