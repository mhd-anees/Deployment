from django.shortcuts import render
from .models import Product,Cart
from django.http import HttpResponse

def product_list(request):
    products = Product.objects.all()
    return render(request, 'home/product_list.html', {'products':products})

def homepage(request):
    return HttpResponse("This is home page")

def cartlist(request):
    cartproducts = Cart.objects.all()
    return render(request, 'home/cart_list.html', {'cartproducts':cartproducts})
