from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# function for the home route

def home(request):
    return render("<h1>Hello From home route</h1>")

def about(request):
    return render(request,"about.html")