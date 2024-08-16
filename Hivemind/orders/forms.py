from django import forms 
from .models import Order


class OrderCreateForm(forms.ModelForm):   
    class Meta:        
        model = Order        
        fields = ['address', 'phone_number']
        widgets = {
            'address': forms.TextInput(attrs={'id':'address','placeholder': 'Delivery address','class': 'w-full py-1 lg:py-2 px-3 rounded-lg lg:rounded-xl border border-red-900 autocomplete-container'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone number eg. 256.....','class': 'w-full py-1 lg:py-22 px-3 rounded-lg lg:rounded-xl border border-red-900'}),
    
        }


