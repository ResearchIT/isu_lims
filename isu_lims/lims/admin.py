from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Genus)
admin.site.register(SubGenus)
admin.site.register(Species)
admin.site.register(Accession)
admin.site.register(Plant)
admin.site.register(SeedPacket)
admin.site.register(Seed)
admin.site.register(Project)