from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Genus)
admin.site.register(models.Subgenus)
admin.site.register(models.Species)
admin.site.register(models.Genome)
admin.site.register(models.Accession)
admin.site.register(models.SeedPacket)
admin.site.register(models.Project)
admin.site.register(models.Sample)
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