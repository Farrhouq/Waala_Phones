from email.policy import default
from enum import unique
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    price = models.FloatField(null=True)
    stock = models.IntegerField(null=True)
    image = models.ImageField(null=True, default='cart.png')
    

    def __str__(self) -> str:
        return self.name

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = set()

    