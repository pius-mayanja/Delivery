from django.urls import path
from . import views

urlpatterns = [
    path('', views.this, name="this"),  # Define your app-specific URLs here
]

rom django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Include the URLs from 'main.urls'
