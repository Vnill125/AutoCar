# Generated by Django 3.2.7 on 2024-01-05 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0037_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='receiver',
            new_name='recipient',
        ),
    ]
