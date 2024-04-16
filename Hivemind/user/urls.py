from django.urls import path 
from .views import *
from django.contrib.auth import views as auth_views
from .forms import LoginForm


app_name = 'user'

urlpatterns = [
    path('signup/', CustomerSignUpView.as_view(), name='signup'),
    path("signup/business/",BusinessSignUpView.as_view(), name="reg"),
    path('login/',LoginView.as_view(), name='login'),
    path('logout/', Logout_view , name='logout'),
    path('sell/', Sell_details, name='sell_details' ),
]