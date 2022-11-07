from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Doctor

# Create your views here.

def home(request : HttpRequest):

   Doctors = Doctor.objects.all()

   return render(request,'home.html',{'Doctors' : Doctors} )


def add_doc(request : HttpRequest):

   if request.method == "POST":
      new_doc = Doctor(name =request.POST["name"], desc = request.POST["desc"], experience = request.POST["experience"], rating = request.POST["rating"])
      new_doc.save()

   
   return render(request, "add_doc.html")

