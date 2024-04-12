from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404, redirect
from .models import Categories, Product, Type
from django.http import HttpResponse
from user.decorators import customer_required
from django.db.models import Q



def items(request):
    categories = Categories.objects.all()[0:8]
    products = Product.objects.all()
    type = Type.objects.all()


    return render(request, 'jumia/item.html', {'categories':categories,
                                                'products': products,
                                                'type': type})
@customer_required
def detail(request, id):
    item = get_object_or_404(Type, pk=id)
    related_items = Type.objects.filter(product=item.product).exclude(pk=id)

    return render(request, 'jumia/detail.html', {
        'item': item,
        'related_items': related_items,
    })






def checkout(request):
    return render(request, 'jumia/cart.html')
                

