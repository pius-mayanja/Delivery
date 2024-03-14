from django.urls import path
from .views import items

app_name = 'jumia'

urlpatterns = [
    path('', items, name='items'),
]