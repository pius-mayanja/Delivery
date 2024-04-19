from django import forms 
from .models import Order


class OrderCreateForm(forms.ModelForm):   
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'First Name',
        'class': 'w-full py-2 px-3 rounded-xl border border-red-900'
    })) 
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Last Name',
        'class': 'w-full py-2 px-3 rounded-xl border border-red-900'
    })) 
    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Email',
        'class': 'w-full py-2 px-3 rounded-xl border border-red-900'
    })) 
    address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'First Name',
        'class': 'w-full py-2 px-3 rounded-xl border border-red-900'
    })) 
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Address',
        'class': 'w-full py-2 px-3 rounded-xl border border-red-900'
    })) 
    city = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'City',
        'class': 'w-full py-2 px-3 rounded-xl border border-red-900'
    }),) 
    class Meta:        
        model = Order        
        fields = ['first_name', 'last_name', 'email', 'address', 'phone_number', 'city']
