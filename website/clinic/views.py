from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
#from .models import Post, Comment

# Create your views here.
def home(request: HttpRequest):

    return render(request, "clinic/homePage.html")

def detailPage(request: HttpRequest):

    return render(request, "clinic/detailPage.html")

def bookingpage(request: HttpRequest):

    return render(request, "clinic/Appointment.html")

def searchBar(request: HttpRequest):

    if "search" in request.GET:
        posts = Post.objects.filter(title__contains=request.GET["search"])
    else:
        posts = Post.objects.all()


    return render(request, "clinic/detailPage.html", {"posts" : posts})        

