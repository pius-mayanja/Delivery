from django.shortcuts import render


def about(request):
    return render(request, 'bus/about.html' )

def sell(request):
    return render(request, 'bus/signup.html' )

def product(request):
    return render(request, 'bus/pdt_mgt.html' )
