
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from jumia.models import Type, Categories
from .models import User, Customer
from django.db import transaction
from django.contrib.auth import get_user_model
from decimal import Decimal

User = get_user_model()

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))


class CustomerSignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First username','class': 'w-full py-4 px-6 rounded-xl'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last username','class': 'w-full py-4 px-6 rounded-xl'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your username','class': 'w-full py-4 px-6 rounded-xl'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Your email address','class': 'w-full py-4 px-6 rounded-xl'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your password','class': 'w-full py-4 px-6 rounded-xl'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password','class': 'w-full py-4 px-6 rounded-xl'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        if commit:
            user.save()
        customer = Customer.objects.create(user=user, first_name=self.cleaned_data.get('first_name'), last_name=self.cleaned_data.get('last_name'),)
        return user

   

class DetailForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['category','name','description','price','image']
        
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Get the user from the kwargs
        super(DetailForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.product_by = self.user  # Set the product_by field to the logged-in user
        if commit:
            instance.save()
        return instance
    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop('user', None)
    #     super().__init__(*args, **kwargs)
    #     if user:
    #         self.fields['product_by'].queryset = User.objects.filter(pk=user.pk)