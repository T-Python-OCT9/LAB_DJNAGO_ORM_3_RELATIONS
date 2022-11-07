from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Doctor, Appointment

# Create your views here.

def add_doctor(request : HttpRequest):
  
    if request.method == "POST":
        new_post = Doctor(name=request.POST["name"], description=request.POST["description"], specialization=request.POST["specialization"], experience_years = request.POST["experience_years"], rating=request.FILES["rating"])
        new_post.save()


    return render(request, "clinic/add_doctor.html")

def list_doctors(request: HttpRequest):

    if "search" in request.GET:
        doctors = Doctor.objects.filter(title__contains=request.GET["search"])
    else:
        doctors = Doctor.objects.all()


    return render(request, "clinic/.html", {"doctors" : doctors})
