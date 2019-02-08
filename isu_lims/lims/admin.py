from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Genus)
admin.site.register(SubGenus)
admin.site.register(Genome)
admin.site.register(Species)
admin.site.register(Sample)
admin.site.register(Project)
admin.site.register(Seed)
admin.site.register(SeedPacket)
admin.site.register(Plant)
admin.site.register(Accession)
