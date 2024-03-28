from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('your cart/', add_cart, name= 'your_cart'),
    path('cart_items/', cart, name= 'cart_items'),
]