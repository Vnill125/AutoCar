# Generated by Django 3.2.7 on 2023-12-26 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0033_auto_20231226_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(choices=[('Abarth', 'Compact'), ('Alfa Romeo', 'Convertible'), ('Aston Martin', 'Coupe'), ('Audi', 'SUV'), ('Bentley', 'Station wagon'), ('BMW', 'Sedan'), ('Chevrolet', 'Van'), ('Chrysler', 'Transporter'), ('Citroen', 'Other'), ('Dacia', 'Compact'), ('Dodge', 'Convertible'), ('Ferrari', 'Coupe'), ('Fiat', 'SUV'), ('Ford', 'Station wagon'), ('GMC', 'Sedan'), ('Honda', 'Van'), ('Hundai', 'Transporter'), ('Infiniti', 'Other'), ('Jaguar', 'Compact'), ('Jeep', 'Convertible'), ('Kia', 'Coupe'), ('Lamborghini', 'SUV'), ('Land Rover', 'Station wagon'), ('Lexus', 'Sedan'), ('Lancia', 'Van'), ('Lotus', 'Transporter'), ('Maserati', 'Other'), ('Mazda', 'Compact'), ('Mercedes-Benz', 'Convertible'), ('Mitsubishi', 'Coupe'), ('Nissa', 'SUV'), ('Opel', 'Station wagon'), ('Peugeot', 'Sedan'), ('Porsche', 'Van'), ('Renault', 'Transporter'), ('Seat', 'Other'), ('Skoda', 'Compact'), ('Subaru', 'Convertible'), ('Suzuki', 'Coupe'), ('Tesla', 'SUV'), ('Toyota', 'Station wagon'), ('Volvo', 'Sedan'), ('Volkswagen', 'Van')], max_length=100),
        ),
    ]