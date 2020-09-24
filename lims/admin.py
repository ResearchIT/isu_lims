from django.contrib import admin

import csv
from django.http import HttpResponse

# Register your models here.
from . import models

#https://books.agiliq.com/projects/django-admin-cookbook/en/latest/export.html
class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

admin.site.register(models.Project)
admin.site.register(models.Herbarium)

class PlantPhotoTabularInline(admin.TabularInline):
    model = models.PlantPhoto
    raw_id_fields = ('plant',)

class HerbariumTabularInline(admin.TabularInline):
    model = models.Herbarium
    raw_id_fields = ('plant',)

@admin.register(models.Plant)
class PlantAdmin(admin.ModelAdmin, ExportCsvMixin):
    inlines = [
        PlantPhotoTabularInline,
        HerbariumTabularInline,
    ]
    autocomplete_fields = ['accession']
    list_display = ['id', 'accession', 'flowering', 'location', 'notes']
    list_display_links = ['id']
    search_fields = ['accession__accession']
    actions = ["export_as_csv"]

@admin.register(models.Accession)
class AccessionAdmin(admin.ModelAdmin):
    search_fields = ['accession']
    list_display = ['id', 'accession', 'genus', 'subgenus', 'genome', 'species']
    list_display_links = ['id']
    list_editable = ['accession']

@admin.register(models.Sample)
class SampleAdmin(admin.ModelAdmin):
    change_list_template = 'admin/lims/sample_change_list.html'
    autocomplete_fields = ['accession']
    list_display = ['id', 'sample', 'accession', 'sranumber', 'strategy', 'sequenceinstrument', 'tissue_type', 'time_point', 'dev_time_point']
    list_display_links = ['id']

@admin.register(models.SeedPacket)
class SeedPacketAdmin(admin.ModelAdmin):
    search_fields = ['accession__accession']
    autocomplete_fields = ['accession']
    list_display = ['id', 'accession', 'parenta', 'parentb', 'quantity', 'datecollected', 'location', 'checkedoutby', 'notes']
    list_display_links = ['id']