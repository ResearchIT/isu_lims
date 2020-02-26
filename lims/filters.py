import django_filters
from . import models

class AccessionsFilter(django_filters.FilterSet):
    accession = django_filters.CharFilter(field_name='accession', label='Search plant name', lookup_expr='contains')
    genus = django_filters.CharFilter(field_name='genus', label='Search genus', lookup_expr='contains')
    subgenus = django_filters.CharFilter(field_name='subgenus', label='Search subgenus', lookup_expr='contains')
    genome = django_filters.CharFilter(field_name='genome', label='Search genome', lookup_expr='contains')
    species = django_filters.CharFilter(field_name='species', label='Search species', lookup_expr='contains')
    alternatenames = django_filters.CharFilter(field_name='alternatenames', label='Search alternate names', lookup_expr='contains')
    class Meta:
        model = models.Accession
        fields = []