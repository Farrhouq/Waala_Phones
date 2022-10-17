from multiprocessing import context
from operator import is_
from tkinter import N
from unicodedata import name
from django.shortcuts import render
from .forms import ProductForm, ProductFormI, ProductImageForm
from .models import Product, User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from . import forms as f
from .models import Cart, Product
from django.db.models import Q



# Create your views here.
def homepage(request):
    search_query = request.GET.get('q') if request.GET.get('q') != None else ''
    is_admin = '(Admin)' if request.user.is_superuser else ''
    try:
        inte = int(search_query)
        productsa = Product.objects.all()
        products = [product for product in productsa if product.price <= inte]
    except:
        products  = Product.objects.filter(
            Q(brand__icontains=search_query) |
            Q(name__icontains=search_query) 
        ) 
    pn = 0
    if request.user.is_authenticated:
        pn = len(request.user.cart.products)
    
    
    context = {'products': products, 'pn': pn, 'page':'home', 'a':is_admin}
    return render(request, 'home.html', context)


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    username = None
    password = None
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

    try:
        our_user = User.objects.get(username=username)
    except:
        messages.error(request, 'The user does not exist!')

    our_user = authenticate(username=username, password=password)

    if our_user != None:
        login(request, our_user)
        return redirect('home')
    else:
        messages.error(request, 'The username or password does not exist!')

    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def register(request):
    page = 'register'
    form = f.UserCreationForm()
    if request.method == 'POST':
        form = f.UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            Cart.objects.create(user = user)
            login(request, user)
            return redirect('home')
    context = {'form': form, 'page': page}
    return render(request, 'register.html', context)


def cart(request):
    page = 'cart'
    cart = request.user.cart
    products1 = cart.products
    products = []

    for p in products1:
        p1 = Product.objects.get(name=p)
        products.append(p1)

    pn = len(products)
    total = cart.calc_price()
    
    context = {'products': set(products), 'pn': pn, 'total':total, 'page':page}
    return render(request, 'cart.html', context)


def add_to_cart(request, pk):
    p1 = Product.objects.get(id=pk)
    cart = request.user.cart
    cart.products.add(p1.name)
    return redirect('home')


def remove_from_cart(request, pk):
    p1 = Product.objects.get(id=pk)
    cart = request.user.cart
    cart.products.remove(p1.name)
    return redirect('cart')


def delete(request, pk):
    if not request.user.is_superuser:
        return redirect('home')
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('home')


def edit(request, pk):
    if not request.user.is_superuser:
        return redirect('home')
    page = 'edit'
    product = Product.objects.get(id=pk)
    form = ProductFormI(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product.save()
        return redirect('home',)
        
        
    context = {'form': form, 'page': page}
    return render(request, 'edit.html', context)


def add(request):
    form = ProductForm()
    if request.method == 'POST':
        name = request.POST.get('name')
        try:
            Product.objects.create(
                name = request.POST.get('name'),
                price = request.POST.get('price'),
                stock = request.POST.get('stock'),
                image = request.POST.get('image')
            )
        except:
            Product.objects.create(
                name = request.POST.get('name'),
                price = request.POST.get('price'),
                stock = request.POST.get('stock'),
            )
        return redirect('home')
    context = {'form':form,}
    return render(request, 'add.html', context)


def info(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'info.html', context)

def edit_image(request, pk):
    page = 'image'
    product = Product.objects.get(id=pk)
    form = ProductImageForm()
    if request.method == 'POST':
        form = ProductImageForm(request.FILES, instance=product)
        if form.is_valid():
            product.image = request.POST.get('image')
            product.save()
            return redirect('home')
    return render(request, 'edit.html', {'page':page, 'form':form})


def buy(request):
    page = 'buy'
    if not request.user.is_authenticated:
        return redirect('home')
    cart = Cart.objects.get(user=request.user)
    total = cart.calc_price()
    return render(request, 'buy.html', {'total':total, 'page': page}) 


def buy_single(request, pk):
    page = 'buy'
    total = Product.objects.get(id=pk).price
    return render(request, 'buy-single.html', {'total':total, 'page': page})