# Generated by Django 4.0.6 on 2022-10-16 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='fone.png', null=True, upload_to=''),
        ),
    ]
