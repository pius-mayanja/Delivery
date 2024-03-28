from django.shortcuts import render
from .cart import Cart 

def add_cart(request, type_id):
    cart = Cart
    cart.add(type_id)

    return render(request, 'cart/cat.html')

def cart(request):
    return render(request, 'cart/cart.html')