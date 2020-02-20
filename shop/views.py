from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return render(request, 'shop/index.html')

def contact(request):
    return render(request, 'shop/index.html')

def status(request):
    return render(request, 'shop/index.html')

def search(request):
    return render(request, 'shop/index.html')

def menu(request):
    return render(request, 'shop/index.html')

def cart(request):
    return render(request, 'shop/index.html')

def checkout(request):
    return render(request, 'shop/index.html')