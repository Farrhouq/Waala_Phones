# Generated by Django 4.0.6 on 2022-09-26 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_product_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
    ]
