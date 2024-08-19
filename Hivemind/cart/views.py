from django.shortcuts import render, redirect, get_object_or_404 
from django.views.decorators.http import require_POST 
from jumia.models import Type 
from .cart import Cart 
from .forms import CartAddProductForm


@require_POST 
def cart_add(request, product_id):    
    cart = Cart(request)    
    product = get_object_or_404(Type, id=product_id)    
    form = CartAddProductForm(request.POST)    
    if form.is_valid():        
        cd = form.cleaned_data        
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])    
    return redirect('jumia:detail',product_id)

@require_POST 
def cart_remove(request, product_id):
        cart = Cart(request)    
        product = get_object_or_404(Type, id=product_id)    
        cart.remove(product)    
        return redirect('cart:cart_detail')

def cart_detail(request):    
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],'update': True})
    return render(request, 'jumia/cart.html', {'cart': cart})



def cart_update(request, product_id):
    cart = Cart(request)
    quantity = int(request.POST.get('quantity', 1))
    product = get_object_or_404(Type, id=product_id)
    cart.add(product=product, quantity=quantity, override_quantity=True)
    return redirect('cart:cart_detail')

