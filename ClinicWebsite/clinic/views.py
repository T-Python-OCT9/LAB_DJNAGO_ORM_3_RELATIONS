from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Doctor, Appointment

# Create your views here.



def home_page (request : HttpRequest):

    return render(request, "clinic/home_page.html")


def list_doctors(request: HttpRequest):

    if "search" in request.GET:
        doctors = Doctor.objects.filter(name__contains=request.GET["search"])
    else:
        doctors = Doctor.objects.all()

    return render(request, "clinic/list_doctors.html", {"doctors": doctors})


def detail_page(request : HttpRequest, doc_id: int):

    try:
        doctor= Doctor.objects.get(pk=doc_id)

    except:
        return render(request, "clinic/not_found.html")
    return render(request, "clinic/detail_page.html", {"doctor": doctor})


def make_appointment(request : HttpRequest):

    return render(request, "clinic/make_appointment.html")


def add_doctor(request: HttpRequest):

    if request.method == "POST":
        new_doctor = Doctor(name=request.POST["name"], description = request.POST["description"],
            specialization=request.POST["specialization"],experience_years=request.POST["experience_years"],
            rating= request.POST["rating"])
        new_doctor.save()

    return render(request, "clinic/add_doc.html")

