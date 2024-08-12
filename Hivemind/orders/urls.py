from django.urls import path 
from .views import *

app_name = 'orders'

urlpatterns = [
    path('created/', order_create, name='order_create'),
    path('orders/', orders, name='order'),
    path('order-details/<int:id>', order_details, name='detail'),
    path('order-delete/<int:id>/delete', delete_order, name='delete_order'),
    path('payment/<int:order_id>/', initiate_payment, name='payment'),
    path('success/', payment_callback, name='payment_callback'),
]

