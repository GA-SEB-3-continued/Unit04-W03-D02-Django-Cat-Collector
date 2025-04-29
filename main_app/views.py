from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


class Cat:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

# Create a list of Cat instances
cats = [
    Cat('Lolo', 'tabby', 'Kinda rude.', 3),
    Cat('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
    Cat('Fancy', 'bombay', 'Happy fluff ball.', 4),
    Cat('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]


# function for the home route

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request,"about.html")

def donate(request):
    return render(request,"donate.html")

def cats_index(request):
    return render(request,"cats/index.html",{"cats":cats})

# Create a donation page
# 1. create the html in the templates file this should contain 1 button <button>donate<button>
# 2. create a views function that should render the donation.html
# 3. add your views to the urls.py file

# 4. BONUS: use the base.html as a partial and display all the content in there