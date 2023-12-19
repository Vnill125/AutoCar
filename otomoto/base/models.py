from django.db import models
from django.core.exceptions import ValidationError

import pytz
import datetime

def validate_registration_year(year):
    if year < 1900 or year > 2024:
        raise ValidationError(
            'Wrong first registration year. Has to be between 1900 and 2024.'
        )

class Car_Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.name)

class Car_Model(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.name)

class Car(models.Model):
    BODY_TYPE = (
        ('Compact', 'Compact'),
        ('Convertible', 'Convertible'),
        ('Coupe', 'Coupe'),
        ('SUV', 'SUV'),
        ('Station wagon', 'Station wagon'),
        ('Sedan', 'Sedan'),
        ('Van', 'Van'),
        ('Transporter', 'Transporter'),
        ('Other', 'Other'),
    )

    FUEL_TYPE = (
        ('Gasoline', 'Gasoline'),
        ('Diesel', 'Diesel'),
        ('LPG', 'LPG'),
        ('Electric', 'Electric'),
    )

    TRANSMISSION_TYPE = (
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic')
    )

    brand = models.ForeignKey(Car_Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Car_Model, on_delete=models.CASCADE)

    body = models.CharField(max_length=255, null=False, blank=False, choices=BODY_TYPE)
    first_registration_year = models.IntegerField(
        null=False, blank=False, default=datetime.datetime.today().year, validators=[validate_registration_year])
    horse_power = models.IntegerField(null=False, blank=False, default=None)
    transmission = models.CharField(max_length=255, choices=TRANSMISSION_TYPE, default=None)
    fuel_type = models.CharField(max_length=255, null=False, blank=False, default='None', choices=FUEL_TYPE)
    price = models.DecimalField(null=False, blank=False, default='0', max_digits=8, decimal_places=0)
    max_price = models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=0)
    description = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=2, choices=pytz.country_names.items(), default=None)
    city = models.CharField(max_length=255, null=False, blank=False, default=None)
    car_images = models.ImageField(default='default_car.jpg')

    def __str__(self):
        return str(self.id)
