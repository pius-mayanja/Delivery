from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import CustomerSignUpForm, SellForm, DetailForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .models import User
from business.forms import BusinessForm, BusinessSignUpForm
import django.contrib.auth.views as auth_views
from django.contrib.auth import login
from user.forms import LoginForm

def SignUp(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = CustomerSignUpForm()

    return render(request, 'user/signup.html', {'form':form})

class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'user/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('jumia:items')

class BusinessSignUpView(CreateView):
    model = User
    form_class = BusinessSignUpForm
    template_name = 'bus/bus_reg.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'business'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/login')

def Logout_view(request):
    logout(request)
    return redirect('/')

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'user/login.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_customer:
                return reverse('jumia:items')
            elif user.is_business:
                return reverse('business:sell')
        else:
            return reverse('/login/')

@login_required
def Sell(request):
    if request.method == 'POST':
        form = SellForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('user:sell_details')
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

