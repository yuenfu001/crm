from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("you are in the index page")

def contact(request):
    return HttpResponse("contact page")