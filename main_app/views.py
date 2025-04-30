from django.shortcuts import render, redirect


# Create your views here.
from django.http import HttpResponse

# importing the cat model
from .models import Cat, Toy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

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

    # Only get the toys the cat does not have
    toys_cat_doesnt_have = Toy.objects.exclude(id__in = cat.toys.all().values_list('id'))

    feeding_form = FeedingForm()
    return render(request, 'cats/detail.html', {
        'cat': cat,
        'feeding_form': feeding_form,
        'toys': toys_cat_doesnt_have  # send those toys
    })


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



class ToyCreate(CreateView):
    model = Toy
    fields = "__all__"


class ToyList(ListView):
    model = Toy

class ToyDetail(DetailView):
    model = Toy

class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'


def associate_toy(request, cat_id, toy_id):
    # Note that you can pass a toy's id instead of the whole object
    Cat.objects.get(id=cat_id).toys.add(toy_id)
    return redirect('cat-detail', cat_id=cat_id)
