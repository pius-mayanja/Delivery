from django.shortcuts import render,redirect, get_object_or_404
from user.decorators import customer_required, business_required
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import BusinessForm
from .models import Business
from jumia.models import Type
from orders.models import OrderItem, Order

def about(request):
    return render(request, 'bus/about.html' )

@business_required
def sell(request):
    business = Business.objects.all()
    return render(request, 'bus/board.html', {'business':business} )

def business_reg(request):
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('business:sell')
    else:
        form = BusinessForm()

    return render(request, 'bus/bus_reg.html', {'form':form})

@business_required
def manage(request):
    items = Type.objects.all()
    return render(request, 'user/manage.html', {'items': items} )


@business_required
@login_required
def detail(request, id):
    item = get_object_or_404(Type, pk=id)
    related_items = Type.objects.filter(category=item.category).exclude(pk=id)

    return render(request, 'bus/detail.html', {
        'item': item,
        'related_items': related_items,
    })

def ordered(request):
    orders = Order.objects.all()
    product = OrderItem.objects.all()
    return render(request, 'bus/ordered.html', {'orders':orders, 'product':product})
