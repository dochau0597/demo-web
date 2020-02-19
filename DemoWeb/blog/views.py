from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    return render(request, 'index.html')

def lienhe(request):
    return render(request, 'lienhe.html')

def login(request):
    return render(request, 'login.html')

def baiviet(request):
    Data = {'Posts':  Post.objects.all().order_by("-date")}
    return render(request, 'baiviet.html', Data)