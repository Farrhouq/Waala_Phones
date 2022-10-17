from tkinter import N
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('register', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logoutUser'),
    path('my_cart', views.cart, name='cart'),
    path('add-to-cart/<str:pk>/', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<str:pk>/', views.remove_from_cart, name='remove-from-cart'),
    path('delete/<str:pk>/', views.delete, name='delete'),
    path('edit/<str:pk>/', views.edit, name='edit'),
    path('add', views.add, name='add'),
    path('edit_image/<str:pk>/', views.edit_image, name='edit_image'),
    path('buy', views.buy, name='buy'),
    path('buy_single/<str:pk>/', views.buy_single , name='buy_single'),
    path('info/<str:pk>/', views.info , name='info'),

]