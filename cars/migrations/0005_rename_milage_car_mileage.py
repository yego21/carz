# Generated by Django 4.2.3 on 2023-07-13 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_car_features'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='milage',
            new_name='mileage',
        ),
    ]
