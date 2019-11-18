import django_filters
from . import models

class AccessionsFilter(django_filters.FilterSet):
    accession = django_filters.CharFilter(field_name='accession', label='Search plant name', lookup_expr='contains')
    genus = django_filters.ModelChoiceFilter(field_name='species.genome.subgenus.genus', queryset=models.Genus.objects.all())
    subgenus = django_filters.ModelChoiceFilter(field_name='species.genome.subgenus', queryset=models.Subgenus.objects.all())
    genome = django_filters.ModelChoiceFilter(field_name='species.genome', queryset=models.Genome.objects.all())
    species = django_filters.ModelChoiceFilter(field_name='species', queryset=models.Species.objects.all())
    alternatenames = django_filters.CharFilter(field_name='alternatenames', label='Search alternate names', lookup_expr='contains')
    class Meta:
        model = models.Accession
        fields = []