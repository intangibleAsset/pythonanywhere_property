import django_filters
from . models import Item

class SearchFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(lookup_expr='icontains')
    seizedLocation = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Item
        fields = ['oic', 'exhibitRef']