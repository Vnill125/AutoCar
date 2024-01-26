# Generated by Django 3.2.7 on 2024-01-02 16:12

import base.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0034_alter_car_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(choices=[('Abarth', 'Abarth'), ('Alfa Romeo', 'Alfa Romeo'), ('Aston Martin', 'Aston Martin'), ('Audi', 'Audi'), ('Bentley', 'Bentley'), ('BMW', 'BMW'), ('Chevrolet', 'Chevrolet'), ('Chrysler', 'Chrysler'), ('Citroen', 'Citroen'), ('Dacia', 'Dacia'), ('Dodge', 'Dodge'), ('Ferrari', 'Ferrari'), ('Fiat', 'Fiat'), ('Ford', 'Ford'), ('GMC', 'GMC'), ('Honda', 'Honda'), ('Hundai', 'Hundai'), ('Infiniti', 'Infiniti'), ('Jaguar', 'Jaguar'), ('Jeep', 'Jeep'), ('Kia', 'Kia'), ('Lamborghini', 'Lamborghini'), ('Land Rover', 'Land Rover'), ('Lexus', 'Lexus'), ('Lancia', 'Lancia'), ('Lotus', 'Lotus'), ('Maserati', 'Maserati'), ('Mazda', 'Mazda'), ('Mercedes-Benz', 'Mercedes-Benz'), ('Mitsubishi', 'Mitsubishi'), ('Nissan', 'Nissan'), ('Opel', 'Opel'), ('Peugeot', 'Peugeot'), ('Porsche', 'Porsche'), ('Renault', 'Renault'), ('Seat', 'Seat'), ('Skoda', 'Skoda'), ('Subaru', 'Subaru'), ('Suzuki', 'Suzuki'), ('Tesla', 'Tesla'), ('Toyota', 'Toyota'), ('Volvo', 'Volvo'), ('Volkswagen', 'Volkswagen'), ('Other', 'Other')], max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='first_registration_year',
            field=models.IntegerField(default=2024, validators=[base.models.validate_registration_year]),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='car',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='car_images/')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='base.car')),
            ],
        ),
    ]