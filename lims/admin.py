from django.contrib import admin

import nested_admin

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

class PlantPhotoTabularInline(nested_admin.NestedTabularInline):
    model = models.PlantPhoto
    raw_id_fields = ('plant',)

class HerbariumTabularInline(nested_admin.NestedTabularInline):
    model = models.Herbarium
    raw_id_fields = ('plant',)

@admin.register(models.Plant)
class PlantAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        PlantPhotoTabularInline,
        HerbariumTabularInline,
    ]