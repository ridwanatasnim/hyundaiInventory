import django_filters
from django_filters import CharFilter
from .models import *


class KitFilter(django_filters.FilterSet):
   
    class Meta:
        model = Kit
        fields= '__all__'

