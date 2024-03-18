from django.shortcuts import render

# Create your views here.


def this(request):
    return render(request, 'index.html')
