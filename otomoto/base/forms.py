from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Car, CarImage


class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2'] 

class CarImageForm(forms.ModelForm):
    class Meta:
        model = CarImage
        fields = ['image']

CarImageFormSet = forms.inlineformset_factory(Car, CarImage, form=CarImageForm, extra=1)

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'body', 'first_registration_year', 'horse_power', 'mileage', 'transmission',
                  'fuel_type', 'price', 'contact_number', 'description', 'country', 'city']

CarImageFormSet = forms.inlineformset_factory(Car, CarImage, form=CarImageForm, extra=10)
