from django.urls import path
from .views import *
from django.contrib.auth.views import *

app_name = 'business'

urlpatterns = [
    path('about/', about, name='about'),
    path('sells/', sell, name='sell'),
    path('manage/', manage, name='manage'),
    path('detail/<int:id>',detail, name= 'detail'),
    path('ordered/',ordered, name= 'ordered'),
    path('products/', business_reg, name='reg'),
]
