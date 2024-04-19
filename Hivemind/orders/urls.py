from django.urls import path 
from .views import *

app_name = 'orders'

urlpatterns = [
    path('created/', order_create, name='order_create'),
    path('orders/', orders, name='order'),
    path('order-details/<int:id>', order_details, name='detail'),
    ]