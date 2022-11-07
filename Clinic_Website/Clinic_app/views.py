import datetime
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import Doctor, Appointment
# .models import
# Create your views here.


def home(request: HttpRequest):

    return render(request, "Clinic_app/home.html")


def add_doctor(request: HttpRequest):
    if request.method == "POST":
        doctors = Doctor(name=request.POST["name"], description=request.POST["description"], specialization=request.POST["specialization"],
                         experience_years=request.POST["experience_years"], rating=request.POST["rating "])
        doctors.save()
        return render(request, "Clinic_app/add_doctors.html")


def show_doctors(request: HttpRequest):
    if "search" in request.GET:
        doctors = Doctor.objects.filter(name__contains=request.GET["search"])
    else:
        doctors = Doctor.objects.all

    return render(request, "Clinic_app/home.html", {" doctors": doctors})


def detail_doctor(request: HttpRequest, doctor_id: int):
    try:
        doctors = Doctor.objects.get(id=doctor_id)
        appointments = Appointment.objects.filter(doctors=doctors)
    except:
        return render(request, "Clinic_app/home.html")

    return render(request, "Clinic_app/detail_doctor.html", {"doctors": doctors, "appointments": appointments})


def delete_doctor(request: HttpRequest, doctor_id: int):
    try:
        doctors = Doctor.objects.get(id=doctor_id)
    except:
        return render(request, "Clinic_app/home.html")
    doctors.delete()

    return redirect("Clinic_app:show_doctors")


def update_doctor(request: HttpRequest, doctor_id: int):
    try:
        doctors = Doctor.objects.get(id=doctor_id)
    except:
        return render(request, "Clinic_app/home.html")

    if request.method == "POST":
        doctors.name = request.POST["name"]
        doctors.description = request.POST["description"]
        doctors.specialization = request.POST["specialization"]
        doctors.experience_years = request.POST["experience_years"]
        doctors.rating = request.POST["rating "]
        doctors.save()

        return redirect("Clinic_app:show_doctors")

    #post.publish_date = post.publish_date.isoformat("T", "hours").replace("+", ":")
    return render(request, "Clinic_app/doctors_update.html", {" doctors":  doctors})


def add_appointment(request: HttpRequest, doctor_id: int):
    doctors = Doctor.objects.get(id=doctor_id)
    if request.method == "POST":
        appointments = Appointment(doctor=doctors, patient_name=request.POST["patient_name"],
                                   case_description=request.POST["case_description"], patient_age=request.POST["patient_age"], appointment_datetime=request.POST["appointment_datetime"], is_attended=request.POST["is_attended"])
        appointments.save()
        return redirect("Clinic_app:detail_doctor", doctor_id)
