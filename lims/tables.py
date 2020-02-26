import django_tables2 as tables
from . import models

class AccessionTable(tables.Table):

    pinumber = tables.Column(accessor='pinumber', verbose_name='Plant ID')
    accession = tables.Column(accessor='accession', verbose_name='Plant Name')
    genus = tables.Column(accessor='genusflat', verbose_name='Genus')
    subgenus = tables.Column(accessor='subgenusflat', verbose_name='Subgenus')
    genome = tables.Column(accessor='genomeflat', verbose_name='Genome')
    species = tables.Column(accessor='speciesflat', verbose_name='Species')
    demoboll = tables.BooleanColumn(accessor='demoboll', verbose_name='Demoboll', yesno='Y,N')
    status = tables.Column(accessor='status', verbose_name='Status')
    alternatenames = tables.Column(accessor='alternatenames', verbose_name='Alternate Names')

    class Meta:
        model = models.Accession
        fields = ()
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