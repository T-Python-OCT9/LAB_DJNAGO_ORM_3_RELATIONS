from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from . models import doctor  #Appointment
# Create your views here.

def add_doctor(request : HttpRequest ):
    if request.method == "POST":
        new_doctor= doctor(name=request.POST["name"], description=request.POST["description"] , specialization =request.POST["specialization"] , experience_years =request.POST["experience_years"] , rating =request.POST["rating"] )
        new_doctor.save()

    return render(request, "ClinicApp/add_doctor.html")


def homepage (requste:HttpRequest):
   

    return render(requste,'ClinicApp/base.html')