from django.urls import path
from . import views

urlpatterns = [
    path('', views.this, name="this"),  # Define your app-specific URLs here
]
