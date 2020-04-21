from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Project)
admin.site.register(models.Herbarium)

class PlantPhotoTabularInline(admin.TabularInline):
    model = models.PlantPhoto
    raw_id_fields = ('plant',)

class HerbariumTabularInline(admin.TabularInline):
    model = models.Herbarium
    raw_id_fields = ('plant',)

@admin.register(models.Plant)
class PlantAdmin(admin.ModelAdmin):
    inlines = [
        PlantPhotoTabularInline,
        HerbariumTabularInline,
    ]
    autocomplete_fields = ['accession']
    list_display = ['accession', 'flowering', 'location', 'notes']
    search_fields = ['accession__accession']

@admin.register(models.Accession)
class AccessionAdmin(admin.ModelAdmin):
    search_fields = ['accession']
    list_display = ['id', 'accession', 'genus', 'subgenus', 'genome', 'species']
    list_display_links = ['id']
    list_editable = ['accession']

@admin.register(models.Sample)
class SampleAdmin(admin.ModelAdmin):
    autocomplete_fields = ['accession']

@admin.register(models.SeedPacket)
class SeedPacketAdmin(admin.ModelAdmin):
    autocomplete_fields = ['accession']