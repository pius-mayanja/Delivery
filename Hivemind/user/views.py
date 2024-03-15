from django.shortcuts import render,redirect
from .forms import SignUpForm
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
    return redirect('/login/')