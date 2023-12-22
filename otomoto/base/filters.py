import django_filters
from django.forms.widgets import TextInput
from .models import Car, Car_Brand, Car_Model

class CarFilter(django_filters.FilterSet):
    max_price = django_filters.NumberFilter(field_name='max_price', lookup_expr='lte', label='Price', widget=TextInput(attrs={'placeholder': 'Price to:'}))
    first_registration_year = django_filters.CharFilter(widget=TextInput(attrs={'placeholder': 'Year:'}))
    
    class Meta:
        model = Car
        fields = ['brand', 'model', 'body', 'first_registration_year', 'horse_power', 'transmission', 'fuel_type', 'price', 'max_price']
        
