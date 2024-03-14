from django.shortcuts import render
from .models import Categories, Product, Type

def items(request):
    categories = Categories.objects.all()
    products = Product.objects.all()
    type = Type.objects.all()

    return render(request, 'jumia\items.html', {'categories':categories,
                                                'products': products,
                                                'type': type})