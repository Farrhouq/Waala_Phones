from django.forms import ModelForm
from . import models
from django.contrib.auth.forms import UserCreationForm

class ProductForm(ModelForm):
    class Meta:
        model = models.Product
        fields = '__all__'

class UserForm(ModelForm):
    class Meta:
        model = models.User
        fields = ['username', 'password']
