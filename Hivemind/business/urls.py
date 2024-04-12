from django.urls import path
from .views import *
from django.contrib.auth.views import *

app_name = 'business'

urlpatterns = [
    path('about/', about, name='about'),
    path('sell/', sell, name='sell'),
    path('products/', business_reg, name='reg'),
]
