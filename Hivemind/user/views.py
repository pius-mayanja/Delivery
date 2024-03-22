from django.shortcuts import render,redirect
from .forms import SignUpForm, SellForm, DetailForm
from django.contrib.auth import logout

def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignUpForm()

    return render(request, 'user/signup.html', {'form':form})


def Logout_view(request):
    logout(request)
    return redirect('/')

def Sell(request):
    if request.method == 'POST':
        form = SellForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/details/')
    else:
        form = SellForm()

    return render(request, 'user/sell.html', {'form':form})


def Sell_details(request):
    if request.method == 'POST':
        form = DetailForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form = DetailForm()

    return render(request, 'user/sell_details.html', {'form':form})
