import django_filters
from django_filters import CharFilter, NumberFilter
from . models import Material

class MaterialFilter(django_filters.FilterSet):


    class Meta:
        model = Material
        fields = ['course', 'semester']
