from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# function for the home route

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request,"about.html")

def donate(request):
    return render(request,"donate.html")


# Create a donation page
# 1. create the html in the templates file this should contain 1 button <button>donate<button>
# 2. create a views function that should render the donation.html
# 3. add your views to the urls.py file

# 4. BONUS: use the base.html as a partial and display all the content in there