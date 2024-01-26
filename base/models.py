from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError


import pytz
import datetime


def validate_registration_year(year):
    if year < 1900 or year > 2024:
        raise ValidationError(
            'Wrong first registration year. Has to be between 1900 and 2024.'
        )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    contact_number = models.CharField(max_length=12, null=True, blank=True)
    
    def __str__(self):
        return self.user.username
       
    
class Car(models.Model):
    BRAND = (
        ('Abarth', 'Abarth'),
        ('Alfa Romeo', 'Alfa Romeo'),
        ('Aston Martin', 'Aston Martin'),
        ('Audi', 'Audi'),
        ('Bentley', 'Bentley'),
        ('BMW', 'BMW'),
        ('Chevrolet', 'Chevrolet'),
        ('Chrysler', 'Chrysler'),
        ('Citroen', 'Citroen'),
        ('Dacia', 'Dacia'),
        ('Dodge', 'Dodge'),
        ('Ferrari', 'Ferrari'),
        ('Fiat', 'Fiat'),
        ('Ford', 'Ford'),
        ('GMC', 'GMC'),
        ('Honda', 'Honda'),
        ('Hundai', 'Hundai'),
        ('Infiniti', 'Infiniti'),
        ('Jaguar', 'Jaguar'),
        ('Jeep', 'Jeep'),
        ('Kia', 'Kia'),
        ('Lamborghini', 'Lamborghini'),
        ('Land Rover', 'Land Rover'),
        ('Lexus', 'Lexus'),
        ('Lancia', 'Lancia'),
        ('Lotus', 'Lotus'),
        ('Maserati', 'Maserati'),
        ('Mazda', 'Mazda'),
        ('Mercedes-Benz', 'Mercedes-Benz'),
        ('Mitsubishi', 'Mitsubishi'),
        ('Nissan', 'Nissan'),
        ('Opel', 'Opel'),
        ('Peugeot', 'Peugeot'),
        ('Porsche', 'Porsche'),
        ('Renault', 'Renault'),
        ('Seat', 'Seat'),
        ('Skoda', 'Skoda'),
        ('Subaru', 'Subaru'),
        ('Suzuki', 'Suzuki'),
        ('Tesla', 'Tesla'),
        ('Toyota', 'Toyota'),
        ('Volvo', 'Volvo'),
        ('Volkswagen', 'Volkswagen'),
        ('Other', 'Other')
    )
    
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

    user = models.ForeignKey(User, default=None ,on_delete=models.CASCADE)
    
    
    brand = models.CharField(max_length=100, choices=BRAND)
    model = models.CharField(max_length=45)
    
    
    body = models.CharField(max_length=255, null=False, blank=False, choices=BODY_TYPE)
    first_registration_year = models.IntegerField(null=False, blank=False, default=datetime.datetime.today().year, validators=[validate_registration_year])
    horse_power = models.IntegerField(null=False, blank=False, default=None)
    mileage = models.IntegerField(default=None ,null= False, blank=False)
    transmission = models.CharField(max_length=255, choices=TRANSMISSION_TYPE, default=None)
    fuel_type = models.CharField(max_length=255, null=False, blank=False, default='None', choices=FUEL_TYPE)
    price = models.DecimalField(null=False, blank=False, default='0', max_digits=8, decimal_places=0)
    max_price = models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=0)
    contact_number = models.CharField(default=None,max_length=12)
    description = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=2, choices=pytz.country_names.items(), default=None)
    city = models.CharField(max_length=255, null=False, blank=False, default=None)
    car_images = models.ImageField(default='default_car.jpg')

    def __str__(self):
        return str(self.id)
    
class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='car_images/')
    
 
class Chat(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    participants = models.ManyToManyField(User)
    
    
    def __str__(self):
        return self.title 
   
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(Chat, default=None, on_delete= models.CASCADE)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.sender} to {self.recipient} - {self.timestamp}'
    
