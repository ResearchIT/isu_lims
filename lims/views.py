from django.views.generic.edit import FormView
from django.shortcuts import render
from django_tables2 import SingleTableView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse

from . import models, tables, filters, forms

def index(request):
    return render(request, 'lims/index.html')

def thanks(request):
    return render(request, 'lims/thanks.html')

class AccessionTableView(PermissionRequiredMixin, SingleTableMixin, FilterView):
    # django
    model = models.Accession
    template_name = "lims/filterable_overview_table_page.html"
    # django-tables2
    table_class = tables.AccessionTable
    # PermissionRequiredMixin
    permission_required = 'lims.view_accession'
    # django-filters
    filterset_class = filters.AccessionsFilter

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

class ImportSamplesAdminView(PermissionRequiredMixin, FormView):
    form_class = forms.SampleImportForm
    permission_required = 'lims.change_sample'
    template_name = "admin/lims/import_samples.html"
    success_url = '/admin/lims/sample/'

    def form_valid(self, form):
        csv_data = form.cleaned_data['csv_file']
        zipped_rejects = form.import_from_csv(csv_data)
        response = HttpResponse(zipped_rejects, content_type='application/zip')
        response['Content-Disposition'] = 'inline;filename=rejects.zip'
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Manually plugging in context variables needed 
        # to display necessary links and blocks in the 
        # django admin. 
        context['title'] = 'Import Samples CSV'
        #context['has_permission'] = True

        return context

class ImportSeedpacketsAdminView(PermissionRequiredMixin, FormView):
    form_class = forms.SeedpacketImportForm
    permission_required = 'lims.change_seedpacket'
    template_name = "admin/lims/import_seedpackets.html"
    success_url = '/admin/lims/seedpacket/'

    def form_valid(self, form):
        csv_data = form.cleaned_data['csv_file']
        zipped_rejects = form.import_from_csv(csv_data)
        response = HttpResponse(zipped_rejects, content_type='application/zip')
        response['Content-Disposition'] = 'inline;filename=rejects.zip'
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Manually plugging in context variables needed 
        # to display necessary links and blocks in the 
        # django admin. 
        context['title'] = 'Import Seedpackets CSV'
        #context['has_permission'] = True

        return context