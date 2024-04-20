from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404, redirect
from .models import Categories,Type
from django.http import HttpResponse
from user.decorators import customer_required,business_required
from django.db.models import Q
from cart.forms import CartAddProductForm
from .forms import SearchForm


def items(request):
    type = Type.objects.all()
    return render(request, 'jumia/item.html', {'type': type,})

def categories(request, id):
    category = get_object_or_404(Categories, pk=id)
    type = Type.objects.filter(category_id=id)
    return render(request, 'jumia/categories.html', {'type': type,
                                                     'category':category})


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


def search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            # Fix the lookup here
            results = Categories.objects.filter(category_name__icontains=query)
            results = Type.objects.filter(name__icontains=query)
            return render(request, 'jumia/search.html', {'results': results, 'query': query})
    else:
        form = SearchForm()
    return render(request, 'jumia/items.html', {'form': form})
