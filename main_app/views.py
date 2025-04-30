from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

# importing the cat model
from .models import Cat

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import FeedingForm

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

    feeding_form = FeedingForm()
    return render(request, 'cats/detail.html',{
        "cat":cat,
        
        'feeding_form':feeding_form})


# Class Based Views

class CatCreate(CreateView):
    model = Cat
    fields = ['name', 'breed', 'description', 'age']
    success_url = "/cats/"


class CatUpdate(UpdateView):
    model = Cat

    fields = ["breed","description","age"]

class CatDelete(DeleteView):
    model = Cat
    success_url = "/cats/"

def add_feeding(request, cat_id):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect('cat-detail', cat_id=cat_id)
