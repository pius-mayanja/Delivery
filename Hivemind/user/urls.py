from django.urls import path 
from .views import *
from django.contrib.auth import views as auth_views
from .forms import LoginForm


app_name = 'user'

urlpatterns = [
    path('signup/', SignUp, name='signup'),
    path('login/', auth_views.LoginView.as_view(authentication_form=LoginForm, template_name='user/login.html'), name='login'),
    path('logout/', Logout_view , name='logout'),
    path('sell/', Sell, name='sell' ),
    path('details/', Sell_details, name='sell_details' ),
]