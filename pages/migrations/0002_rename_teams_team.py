# Generated by Django 4.2.3 on 2023-07-10 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Teams',
            new_name='Team',
        ),
    ]