from tkinter import N
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('register', views.register, name='register'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('my_cart/<str:pk>', views.cart, name='cart'),
    path('add-to-cart/<str:pk>/', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<str:pk>/', views.remove_from_cart, name='remove-from-cart'),
    path('delete/<str:pk>/', views.delete, name='delete'),
    path('edit/<str:pk>/', views.edit, name='edit'),
    path('add', views.add, name='add'),
]