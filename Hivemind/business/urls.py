from django.urls import path
from .views import *
from django.contrib.auth.views import *

app_name = 'business'

urlpatterns = [
    path('', manage, name='manage'),
    path('detail/<int:id>',detail, name= 'detail'),
    path('orders/',orders, name= 'ordered'),
    path('order-details/<int:id>',order_details, name= 'order_details'),
    path('products/', business_reg, name='reg'),
    path('inbox/',inbox, name='inbox'),
    path('<int:pk>/',cdetail, name='cdetail'),
]
