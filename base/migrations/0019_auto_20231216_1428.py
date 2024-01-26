# Generated by Django 3.2.7 on 2023-12-16 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_auto_20231216_1427'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Car_Brands',
            new_name='Car_Brand',
        ),
        migrations.AlterField(
            model_name='car',
            name='body',
            field=models.CharField(choices=[('Coupe', 'Coupe'), ('Sedan', 'Sedan'), ('Van', 'Van'), ('Convertible', 'Convertible'), ('Transporter', 'Transporter'), ('Compact', 'Compact'), ('SUV', 'SUV'), ('Other', 'Other'), ('Station wagon', 'Station wagon ')], max_length=255),
        ),
        migrations.AlterField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(choices=[('Gasoline', 'Gasoline'), ('Diesel', 'Diesel'), ('Electric', 'Electric'), ('LPG', 'LPG')], default='None', max_length=255),
        ),
    ]