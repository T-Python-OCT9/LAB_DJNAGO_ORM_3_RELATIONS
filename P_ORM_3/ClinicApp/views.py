from django.shortcuts import render ,redirect
from django.http import HttpRequest , HttpResponse
from models import Doctor
# Create your views here.
def add_Doctors(request:HttpRequest):
    if request.method == "POST":
        new_Doctors = Doctor (name=request.POST["name"], description = request.POST["description"], specialization=request.POST["specialization"], experience_years = request.POST["experience_years"],rating=request.POST["rating"])
        new_Doctors.save()

    return render(request,"ClinicApp/add_doctors.html")