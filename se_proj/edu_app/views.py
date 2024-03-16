from django.shortcuts import render

def index(request):

    context = { 

    }

    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')
