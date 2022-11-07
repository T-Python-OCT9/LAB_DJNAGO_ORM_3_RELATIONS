from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Doctor

# Create your views here.
def home(request : HttpRequest):
    
    return render(request, "WebsiteApp/index.html")

def gallary(request : HttpRequest):
    
    return render(request, "WebsiteApp/gallary.html")
def add_doctor(request : HttpRequest):
    if request.method == "POST":
        new_doc = Doctor(Docname=request.POST["Docname"], DocDescrip = request.POST["DocDescrip"], DocRate=request.POST["Doctor_Rate"], experience_years = request.POST["experience_years"],DocSpecialization=request.POST["DocSpecialization"])
        new_doc.save()
    
    return render(request, "WebsiteApp/add_doctor.html")
def doctor_list(request :HttpRequest):
    if "search" in request.GET:
        doctors = Doctor.objects.filter(Docname__contains=request.GET["search"])
    else:
        doctors = Doctor.objects.all()
        return render(request, "WebsiteApp/doctor_list.html", {"doctors" : doctors})
def doctor_detail(request : HttpRequest, doctor_id : int):

    try:
        doctor = Doctor.objects.get(id=doctor_id)
    except:
        return render(request , "WebsiteApp/notFound.html")

    return render(request, "WebsiteApp/doctor_detail.html", {"doctor" : doctor})