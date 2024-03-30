from django.contrib import admin
from .models import Business
from .forms import BusinessForm

admin.site.register(Business)
