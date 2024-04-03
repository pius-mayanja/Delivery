from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import BusinessForm
from .models import Business

def about(request):
    return render(request, 'bus/about.html' )

@login_required
def sell(request):
    business = Business.objects.all()
    return render(request, 'bus/dash.html', {'business':business} )

@login_required
def business_reg(request):
    if request.method == 'POST': 
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('business:sell')
    else:
        form = BusinessForm()
        return render(request, 'bus/bus_reg.html', {'form':form} )

