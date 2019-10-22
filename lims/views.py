from django.shortcuts import render
from django_tables2 import SingleTableView
from django_tables2.views import SingleTableMixin

from . import models, tables

def index(request):
    return render(request, 'lims/index.html')

def thanks(request):
    return render(request, 'lims/thanks.html')

class GeneraTableView(SingleTableView):
    # django
    model = models.Genus
    template_name = "lims/filterable_overview_table_page.html"
    # django-tables2
    table_class = tables.GeneraTable

class SubGeneraTableView(SingleTableView):
    # django
    model = models.Subgenus
    template_name = "lims/filterable_overview_table_page.html"
    # django-tables2
    table_class = tables.SubGeneraTable

class GenomeTableView(SingleTableView):
    # django
    model = models.Genome
    template_name = "lims/filterable_overview_table_page.html"
    # django-tables2
    table_class = tables.GenomeTable

class SpeciesTableView(SingleTableView):
    # django
    model = models.Species
    template_name = "lims/filterable_overview_table_page.html"
    # django-tables2
    table_class = tables.SpeciesTable

class AccessionTableView(SingleTableView):
    # django
    model = models.Accession
    template_name = "lims/filterable_overview_table_page.html"
    # django-tables2
    table_class = tables.AccessionTable

class ProjectTableView(SingleTableView):
    # django
    model = models.Project
    template_name = "lims/filterable_overview_table_page.html"
    # django-tables2
    table_class = tables.ProjectTable

class PlantTableView(SingleTableView):
    # django
    model = models.Plant
    template_name = "lims/filterable_overview_table_page.html"
    # django-tables2
    table_class = tables.PlantTable

class SeedPacketTableView(SingleTableView):
    # django
    model = models.SeedPacket
    template_name = "lims/filterable_overview_table_page.html"
    # django-tables2
    table_class = tables.SeedPacketTable

class SampleTableView(SingleTableView):
    # django
    model = models.Sample
    template_name = "lims/filterable_overview_table_page.html"
    # django-tables2
    table_class = tables.SampleTable

class HerbariumTableView(SingleTableView):
    # django
    model = models.Herbarium
    template_name = "lims/filterable_overview_table_page.html"
    # django-tables2
    table_class = tables.HerbariumTable