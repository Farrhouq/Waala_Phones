# Generated by Django 4.0.6 on 2022-09-27 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_cart_user_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='name',
        ),
    ]
