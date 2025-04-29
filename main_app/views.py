from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# importing the cat model
from .models import Cat


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

# Create a donation page
# 1. create the html in the templates file this should contain 1 button <button>donate<button>
# 2. create a views function that should render the donation.html
# 3. add your views to the urls.py file

# 4. BONUS: use the base.html as a partial and display all the content in there