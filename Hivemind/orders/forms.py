from django import forms 
from .models import Order


class OrderCreateForm(forms.ModelForm):   
    class Meta:        
        model = Order        
        fields = ['first_name', 'last_name', 'address', 'phone_number']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name (uppercass)', 'class': 'w-full py-1 lg:py-2 px-3 rounded-xl border border-red-900'}),
            'address': forms.TextInput(attrs={'id':'address','placeholder': 'Delivery address','class': 'w-full py-1 lg:py-2 px-3 rounded-xl border border-red-900 autocomplete-container'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name (uppercase)','class': 'w-full py-1 lg:py-2 px-3 rounded-xl border border-red-900'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone number eg. 256.....','class': 'w-full py-1 lg:py-22 px-3 rounded-xl border border-red-900'}),
    
        }

