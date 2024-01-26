# Generated by Django 3.2.7 on 2023-12-13 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20231213_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_images',
            field=models.ImageField(default='static/images/default_car.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='car',
            name='body',
            field=models.CharField(choices=[('CU', 'Coupe'), ('T', 'Transporter'), ('O', 'Other'), ('V', 'Van'), ('C', 'Compact'), ('SE', 'Sedan'), ('CO', 'Convertible'), ('S', 'SUV'), ('SW', 'Station wagon ')], max_length=255),
        ),
        migrations.AlterField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(choices=[('G', 'Gasoline'), ('L', 'LPG'), ('E', 'Electric'), ('D', 'Diesel')], default='None', max_length=255),
        ),
    ]