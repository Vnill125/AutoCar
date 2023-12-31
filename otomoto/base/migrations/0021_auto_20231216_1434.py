# Generated by Django 3.2.7 on 2023-12-16 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_auto_20231216_1433'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car_brand',
            old_name='brand',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='car_model',
            old_name='model',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='car',
            name='body',
            field=models.CharField(choices=[('Transporter', 'Transporter'), ('Other', 'Other'), ('Van', 'Van'), ('Station wagon', 'Station wagon '), ('SUV', 'SUV'), ('Sedan', 'Sedan'), ('Convertible', 'Convertible'), ('Coupe', 'Coupe'), ('Compact', 'Compact')], max_length=255),
        ),
        migrations.AlterField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(choices=[('Electric', 'Electric'), ('Gasoline', 'Gasoline'), ('Diesel', 'Diesel'), ('LPG', 'LPG')], default='None', max_length=255),
        ),
    ]
