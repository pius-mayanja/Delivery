from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404, redirect
from .models import Categories, Product, Type
from django.http import HttpResponse




def items(request):
    categories = Categories.objects.all()
    products = Product.objects.all()
    type = Type.objects.all()

    return render(request, 'jumia/items.html', {'categories':categories,
                                                'products': products,
                                                'type': type})
@login_required
def detail(request, id):
    item = get_object_or_404(Type, pk=id)
    related_items = Type.objects.filter(Category=item.Category).exclude(pk=id)

    return render(request, 'jumia/detail.html', {
        'item': item,
        'related_items': related_items
    })



                

