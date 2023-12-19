import django_filters
from .models import Car

class CarFilter(django_filters.FilterSet):
    max_price = django_filters.NumberFilter(field_name='max_price', lookup_expr='lte')

    class Meta:
        model = Car
        fields = ['brand', 'model', 'body', 'first_registration_year', 'horse_power', 'transmission', 'fuel_type', 'price', 'max_price']
