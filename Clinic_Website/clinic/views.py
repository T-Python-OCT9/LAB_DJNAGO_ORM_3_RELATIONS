from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request : HttpResponse):
    if request.method == "POST":
        rating = float ( request.POST["quantity"] )
        print(rating.__class__)
    return render(request,"clinic/home.html")