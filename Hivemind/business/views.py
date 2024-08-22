from django.shortcuts import render,redirect, get_object_or_404
from user.decorators import customer_required, business_required
from django.contrib.auth.decorators import login_required
from .forms import BusinessForm
from .models import Business
from jumia.models import Type
from orders.models import OrderItem, Order
from .forms import ConversationMessageForm
from chart.models import Conversation
from user.models import User, Customer

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
    return render(request, 'bus/manage.html', {'items': items} )


@business_required
@login_required
def detail(request, id):
    item = get_object_or_404(Type, pk=id)
    related_items = Type.objects.filter(category=item.category).exclude(pk=id)

    return render(request, 'bus/detail.html', {
        'item': item,
        'related_items': related_items,
    })

@business_required
def orders(request):
    orders = Order.objects.all()
    return render(request, 'bus/orders.html', {'orders':orders,})

@business_required
def order_details(request, id):
    orders = Order.objects.filter(id=id).first()
    product = OrderItem.objects.filter(order=orders)
    return render(request, 'bus/ordered.html', {'orders':orders, 'product':product})


@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    return render(request, 'bus/inbox.html', {
        'conversations': conversations
    })

@login_required
def cdetail(request, pk):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()

            return redirect('business:cdetail', pk=pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'bus/cdetail.html', {
        'conversation': conversation,
        'form': form
    })