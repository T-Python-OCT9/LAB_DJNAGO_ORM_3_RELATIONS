from django.shortcuts import redirect, render
from django.http import HttpRequest , HttpResponse
from .models import *
# Create your views here.

def home (request :HttpRequest):
       return render(request  , "clinic/home.html")



def all_doctors(request :HttpRequest):
       return render(request  , "clinic/all_doctors.html")
 

def add_new_doctor(request :HttpRequest):
    spec = Doctor.specialization
    if request.method == "POST":
        new_post = Doctor(name=request.POST["name"], description = request.POST["description"], rating=request.POST["rating"], experience_years = request.POST["experience_years"] , specialization=request.POST["specialization"])
        new_post.save()
    return render(request  , "clinic/add_doctor.html" , {"spec" : spec})


def list_doctors(request :HttpRequest):
       if "search" in request.GET:
        details_name = Doctor.objects.filter(name__contains=request.GET["search"])
       else:
        details_name = Doctor.objects.all()

       return render(request, "clinic/doctor_detail.html", {"doctor" : details_name})



def appointments(request :HttpRequest):
   if request.method == "POST":
        new_appointment = Appointment(patient_name = request.POST ["patient_name"] , case_description = request.POST ["case_description"] ,patient_age = request.POST["patient_age"] ,appointment_datetime = request.POST["appointment_datetime"] , is_attended = request.POST ["is_attended"] )
        new_appointment.save()
        return redirect("clinic:home")
   return render(request , "clinic/appointment.html")

