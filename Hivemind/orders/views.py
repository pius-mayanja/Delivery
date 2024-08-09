from django.shortcuts import render,get_object_or_404, redirect
from .models import OrderItem , Order
from django.http import HttpResponseBadRequest
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from user.decorators import customer_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@customer_required
def order_create(request):  
    user = request.user
    if user.is_authenticated:
        cart = Cart(request)
        if request.method == 'POST':        
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                order.user = request.user  
                order = form.save()            
                for item in cart:                
                    OrderItem.objects.create(order=order, product=item['product'], price=item['price'],quantity=item['quantity'])        
                cart.clear()
            return render(request,'order/created.html', {'order': order})    
        else:        
            form = OrderCreateForm()    
        return render(request, 'jumia/checkout.html',{'cart': cart,'form': form,})

@login_required
def delete_order(request,id):
    delete_order = get_object_or_404(Order, id=id)

    if delete_order.user != request.user:
        return HttpResponseBadRequest("You do not have permission to delete this order.")

    if request.method == 'POST':
        delete_order.delete()
        return redirect('orders:order')
        
@customer_required
def orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order/orders.html', {'orders':orders})

@customer_required
def order_details(request, id):
    orders = Order.objects.filter(id=id).filter(user=request.user).first()
    product = OrderItem.objects.filter(order=orders)
    return render(request, 'order/order_details.html', {'orders':orders, 'product':product})



