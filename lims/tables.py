import django_tables2 as tables
from . import models

class GeneraTable(tables.Table):

    class Meta:
        model = models.Genus
        template_name = 'django_tables2/bootstrap.html'

class SubGeneraTable(tables.Table):

    class Meta:
        model = models.Subgenus
        template_name = 'django_tables2/bootstrap.html'

class GenomeTable(tables.Table):

    class Meta:
        model = models.Genome
        template_name = 'django_tables2/bootstrap.html'

class SpeciesTable(tables.Table):

    class Meta:
        model = models.Species
        template_name = 'django_tables2/bootstrap.html'

class AccessionTable(tables.Table):

    class Meta:
        model = models.Accession
        template_name = 'django_tables2/bootstrap.html'
        
class ProjectTable(tables.Table):

    class Meta:
        model = models.Project
        template_name = 'django_tables2/bootstrap.html'
        
class PlantTable(tables.Table):

    class Meta:
        model = models.Plant
        template_name = 'django_tables2/bootstrap.html'
        
class SeedPacketTable(tables.Table):

    class Meta:
        model = models.SeedPacket
        template_name = 'django_tables2/bootstrap.html'
        
class SampleTable(tables.Table):

    class Meta:
        model = models.Sample
        template_name = 'django_tables2/bootstrap.html'
        
class HerbariumTable(tables.Table):

    class Meta:
        model = models.Herbarium
        template_name = 'django_tables2/bootstrap.html'