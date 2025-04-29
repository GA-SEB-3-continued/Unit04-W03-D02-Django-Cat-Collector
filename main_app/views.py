from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# importing the cat model
from .models import Cat

from django.views.generic.edit import CreateView


# function for the home route

def home(request):
    return render(request, "home.html")

def about(request):
    print(Cat.objects.filter(age__lte=3)
)
    return render(request,"about.html")

def donate(request):
    return render(request,"donate.html")

def cats_index(request):
    cats = Cat.objects.all()
    return render(request,"cats/index.html",{"cats":cats})

def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html',{"cat":cat})


# Class Based Views

class CatCreate(CreateView):
    model = Cat
    fields = ['name', 'breed', 'description', 'age']
    success_url = "/cats/"
