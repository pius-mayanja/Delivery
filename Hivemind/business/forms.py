from django import forms
from .models import Business
from django.contrib.auth.forms import UserCreationForm
from user.models import User
from django.db import transaction
from chart.models import ConversationMessage

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = '__all__'



class BusinessSignUpForm(UserCreationForm):    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
  

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_business = True
        if commit:
            user.save()
        business = Business.objects.create(user=user, username=self.cleaned_data.get('username'), email=self.cleaned_data.get('email'), phone_number=self.cleaned_data.get('phone_number'))
        return user
    
class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            })
        }