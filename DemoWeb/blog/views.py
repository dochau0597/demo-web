from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def lienhe(request):
    return render(request, 'lienhe.html')

def login(request):
    return render(request, 'login.html')
