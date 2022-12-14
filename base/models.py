from email.policy import default
from enum import unique
from random import choices
from tkinter import CASCADE
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    price = models.FloatField()
    stock = models.IntegerField(null=True)
    image = models.ImageField(null=True, )
    brand_choices = (
        ('Samsung', 'Samsung'),
        ('Tecno', 'Tecno'),
        ('Nokia', 'Nokia'),
        ('Iphone', 'Iphone'),
    )
    brand = models.CharField(max_length=50, choices=brand_choices, null=True)
    description = models.CharField(max_length=2000, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = set()
    

    def calc_price(self):
        total = 0
        for _ in self.products:
            product = Product.objects.get(name=_)
            total += product.price 
        return total
