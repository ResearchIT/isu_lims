from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Genus)
admin.site.register(SubGenus)
<<<<<<< HEAD
admin.site.register(Genome)
admin.site.register(Species)
admin.site.register(Sample)
admin.site.register(Project)
admin.site.register(Seed)
admin.site.register(SeedPacket)
admin.site.register(Plant)
admin.site.register(Accession)
=======
admin.site.register(Species)
admin.site.register(Accession)
admin.site.register(Plant)
admin.site.register(SeedPacket)
admin.site.register(Seed)
admin.site.register(Project)
>>>>>>> 944f8154a76e213ba3966cd7d1afda05de34039e
