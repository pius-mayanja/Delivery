from django.urls import path, include
from .views import *
from django.contrib.auth.views import *


app_name = 'jumia'

urlpatterns = [
    path('', items, name='items'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('detail/<int:id>',detail, name= 'detail'),

]
