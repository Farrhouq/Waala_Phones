# Generated by Django 4.0.6 on 2022-09-26 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_prod'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Prod',
            new_name='Product',
        ),
    ]
