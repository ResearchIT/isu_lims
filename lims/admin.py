from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Genus)
admin.site.register(models.Subgenus)
admin.site.register(models.Species)
admin.site.register(models.Genome)
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

@admin.register(models.Accession)
class AccessionAdmin(admin.ModelAdmin):
    search_fields = ['accession']
    list_display = ['accession', 'genusflat', 'subgenusflat', 'genomeflat', 'speciesflat']

@admin.register(models.Sample)
class SampleAdmin(admin.ModelAdmin):
    autocomplete_fields = ['accession']

@admin.register(models.SeedPacket)
class SeedPacketAdmin(admin.ModelAdmin):
    autocomplete_fields = ['accession']