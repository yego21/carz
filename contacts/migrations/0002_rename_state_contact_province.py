# Generated by Django 4.2.3 on 2023-07-27 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='state',
            new_name='province',
        ),
    ]