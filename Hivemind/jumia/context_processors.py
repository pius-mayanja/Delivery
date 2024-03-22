from .models import Categories
from django.shortcuts import render

def categories(request):
    cat = Categories.objects.all()
    return {'cat': cat}
