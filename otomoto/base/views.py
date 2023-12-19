from django.shortcuts import render
from .models import Car
from .filters import CarFilter

def index(request):
    filter = CarFilter(request.GET, queryset=Car.objects.all())
    cars = filter.qs

    order_by_options = {
        '1': 'price',
        '2': '-price',
        '3': 'horse_power',
        '4': '-horse_power',
        '5': 'first_registration_year',
        '6': '-first_registration_year',
    }

    order_by_param = request.GET.get('order_by', '-first_registration_year')

    if 'brand' in filter.data:
        order_by_param += f'&brand={filter.data["brand"]}'
        if 'model' in filter.data:
                order_by_param += f'&model={filter.data["model"]}'
        if 'body' in filter.data:
                order_by_param += f'&body={filter.data["body"]}'
        if 'first_registration_year' in filter.data:
                order_by_param += f'&first_registration_year={filter.data["first_registration_year"]}'
        if 'fuel_type' in filter.data:
                order_by_param += f'&fuel_type={filter.data["fuel_type"]}'
        if 'max_price' in filter.data:
                order_by_param += f'&max_price={filter.data["max_price"]}'

    order_by_param = order_by_param.lstrip('&')
            
    cars = cars.order_by(order_by_options.get(order_by_param, '-first_registration_year'))
    

    return render(request, 'index.html', context={'cars': cars, 'filter': filter, 'order_by': order_by_param})
    