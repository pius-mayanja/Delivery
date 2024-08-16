from django.shortcuts import render,get_object_or_404, redirect
from .models import OrderItem , Order
from django.http import HttpResponse, HttpResponseBadRequest
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from user.decorators import customer_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from twilio.rest import Client
import requests
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Payment, Order
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Payment
import re 
from user.models import Customer
from jumia.models import Type

@customer_required
def order_create(request):  
    user = request.user
    if user.is_authenticated:
        customer = Customer.objects.get(user=user)
        cart = Cart(request)
        if request.method == 'POST':      
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                order.user = request.user  
                order = form.save()     
                # accountSID = 'ACe6d928ec56d8f0c7bce4f4301f592d45'
                # authToken = '59519c547005d51047167550327627e5'
                # twilioCli = Client(accountSID, authToken)
                # myTwilioNumber = '+13345083970'
                # myCellPhone = '+256761420297'
                # message = twilioCli.messages.create(body=f'Order was created by {user.first_name}', from_=myTwilioNumber, to=myCellPhone)
                for item in cart:                
                    OrderItem.objects.create(order=order, product=item['product'], price=item['price'],quantity=item['quantity'])        
                cart.clear()
            return render(request,'order/created.html', {'order': order})    
        else:        
            form = OrderCreateForm()    
        return render(request, 'jumia/checkout.html',{'cart': cart,'form': form,'customer':customer})

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
    customer = Customer.objects.get(user=request.user)
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order/orders.html', {'orders':orders,'customer':customer})

@customer_required
def order_details(request, id):
    orders = Order.objects.filter(id=id).filter(user=request.user).first()
    product = OrderItem.objects.filter(order=orders)
    return render(request, 'order/order_details.html', {'orders':orders, 'product':product})


def initiate_payment(request, order_id):
    phone_exp = re.compile(r'(0)(/d{9})')
    if request.method == 'POST':
        
        url = 'https://www.easypay.co.ug/api/'
        secret = 'd58fadc8a79ed090'
        client_id = '317caec39c6e050c'
        
        order = get_object_or_404(Order, id=order_id)
        amount = int(order.cost())
        # if order.phone_number == phone_exp.findall():
            
        try:
            payload = {
                "username": client_id,
                "password": secret,
                "action":"mmdeposit",
                'amount': amount,
                'currency': 'UGX',
                'phone': str(order.phone_number),
                'reference': f'order_{order.id}'
            }
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.post(url, json=payload, headers=headers)

            data = response.json()
            if response.status_code == 200 and data.get('success'):
                Payment.objects.create(order=order, amount=amount, status='Pending', transaction_id=data['transaction_id'])
                return JsonResponse({'status': 'success', 'transaction_id': data['transaction_id']})
            else:
                error_message = data.get('errormsg', 'Unknown error occurred')
                return JsonResponse({'status': 'error', 'message': error_message})
        except Exception as e:
            return JsonResponse({'success': False, 'errormsg': str(e)})
    return JsonResponse({'success': False, 'errormsg': 'Invalid request method'})

    
@csrf_exempt
def payment_callback(request):
    if request.method == 'POST':
        data = request.json()
        transaction_id = data.get('transaction_id')
        status = data.get('status')

        payment = Payment.objects.get(transaction_id=transaction_id)
        payment.status = status
        payment.save()

        if status == 'Completed':
            # Update order status, notify customer, etc.
            pass

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'}, status=400)
