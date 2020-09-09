from django.shortcuts import render
from django.http import HttpResponse

from .models import *
# Create your views here.
def home(request):
    return render(request, "acct/dashboard.html")

def customer(request):
    return render(request, "acct/customer.html")

def navbar(request):
    return render(request, "acct/navbar.html")

def products(request):
    products = Product.objects.all()

    return render(request, "acct/products.html",{"products":products})

def status(request):
    return render(request, "acct/status.html")