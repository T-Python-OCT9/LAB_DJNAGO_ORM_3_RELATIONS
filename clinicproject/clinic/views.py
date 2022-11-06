from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import render, redirect
from .models import Doctor, Appointment

# Create your views here.

def home(request:HttpRequest):
    
    return render(request, 'clinic/base.html')


def add_doctor(request:HttpRequest):
    if request.method == "POST":
        new_doctor = Doctor(name=request.POST.get('name'), description= request.POST.get('description'),specialization = request.POST.get('specialization') ,experience_years= request.POST.get('experience_years'),rating= request.POST.get('rating'))
        new_doctor.save()

        # return redirect("blog:list_post")

    return render(request, "clinic/add_doctors.html")


def doctors(request:HttpRequest):

    if "search" in request.GET:
        doctors = Doctor.objects.filter(name__contains=request.GET["search"])
    else:
        doctors = Doctor.objects.all()

    return render(request, "clinic/list_doctors.html", {"doctors" : doctors})


def view_doctor(request:HttpRequest, doctor_id: int):
    try:
        doctor = Doctor.objects.get(id=doctor_id)
    except:
        return render(request, "clinic/not_found.html")

    context = {'doctor': doctor}
    return render(request, "clinic/view_doctor.html", context)
