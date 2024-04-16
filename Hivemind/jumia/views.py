from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404, redirect
from .models import Categories,Type
from django.http import HttpResponse
from user.decorators import customer_required,business_required
from django.db.models import Q
from cart.forms import CartAddProductForm


def items(request):
    categories = Categories.objects.all()[0:8]
    type = Type.objects.all()
    

    return render(request, 'jumia/item.html', {'categories':categories,'type': type,})


@customer_required
def detail(request, id):
    item = get_object_or_404(Type, pk=id)
    related_items = Type.objects.filter(category=item.category).exclude(pk=id)
    cart_product_form = CartAddProductForm()

    return render(request, 'jumia/detail.html', {
        'item': item,
        'related_items': related_items,
        'cart_product_form':cart_product_form,
    })






def checkout(request):
    return render(request, 'jumia/checkout.html')
                

