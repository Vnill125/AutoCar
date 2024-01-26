from django.contrib import admin

from .models import Car, Profile, CarImage, Message, Chat
# Register your models here.

admin.site.register(Car)
admin.site.register(Profile)
admin.site.register(CarImage)
admin.site.register(Message)
admin.site.register(Chat)
