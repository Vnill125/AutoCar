from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Car, CarImage, Profile


class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2'] 

class CarImageForm(forms.ModelForm):
    class Meta:
        model = CarImage
        fields = ['image']

    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields['image'].widget.attrs.update({'class': 'image_form'})
        
CarImageFormSet = forms.inlineformset_factory(Car, CarImage, form=CarImageForm, extra=1)

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'body', 'first_registration_year', 'horse_power', 'mileage', 'transmission',
                  'fuel_type', 'price', 'contact_number', 'description', 'country', 'city']
        
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields['brand'].widget.attrs.update({'class': 'order_button'})
       self.fields['model'].widget.attrs.update({'class': 'order_button'})
       self.fields['body'].widget.attrs.update({'class': 'order_button'})
       self.fields['first_registration_year'].widget.attrs.update({'class': 'order_button'})
       self.fields['horse_power'].widget.attrs.update({'class': 'order_button'})
       self.fields['mileage'].widget.attrs.update({'class': 'order_button'})
       self.fields['transmission'].widget.attrs.update({'class': 'order_button'})
       self.fields['fuel_type'].widget.attrs.update({'class': 'order_button'})
       self.fields['price'].widget.attrs.update({'class': 'order_button'})
       self.fields['contact_number'].widget.attrs.update({'class': 'order_button'})
       self.fields['description'].widget.attrs.update({'class': 'order_button1'})
       self.fields['country'].widget.attrs.update({'class': 'order_button'})
       self.fields['city'].widget.attrs.update({'class': 'order_button'})

CarImageFormSet = forms.inlineformset_factory(Car, CarImage, form=CarImageForm, extra=10)

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [ 'birth_date', 'contact_number','bio']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'bio'}),
            'birth_date': forms.DateInput(attrs={'class': 'birth_date', 'placeholder':'2024-01-22'}),
            'contact_number': forms.DateInput(attrs={'class': 'contact_number'}),
        }
        