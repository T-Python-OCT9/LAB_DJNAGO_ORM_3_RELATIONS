from django.shortcuts import render ,redirect
from django.http import HttpRequest 
from .models import Doctor ,Appointment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request:HttpRequest):

    return render(request, 'ClinicApp/base.html')

def add_Doctors(request:HttpRequest):
    if request.method == "POST":
        new_Doctors = Doctor (name=request.POST["name"], description = request.POST["description"], specialization=request.POST["specialization"], experience_years = request.POST["experience_years"],rating=request.POST["rating"])
        new_Doctors.save()

    return render(request,"ClinicApp/add_doctors.html")
    

def doctors(request:HttpRequest):

    if "search" in request.GET:
        doctors = Doctor.objects.filter(name__contains=request.GET["search"])
    else:
        doctors = Doctor.objects.all()

    return render(request, "ClinicApp/list_doctors.html", {"doctors" : doctors})

def view_doctor(request:HttpRequest, doctor_id: int):
    try:
        doctor = Doctor.objects.get(id=doctor_id)
        appointments = Appointment.objects.filter(doctor = doctor)
    except:
        return render(request, "ClinicApp/not_found.html")

    context = {'doctor': doctor, 'appointments': appointments}
    return render(request, "ClinicApp/view_doctor.html", context)

def appointment(request:HttpRequest, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    return render(request, "ClinicApp/appointment.html",{'doctor': doctor})

def add_appointment(request:HttpRequest, doctor_id: int):
    doctor = Doctor.objects.get(id=doctor_id)
    if request.method == "POST":
        new_appointment = Appointment(doctor=doctor,pationt_name=request.POST.get('pationt_name'), case_description= request.POST.get('case_description'),patient_age = request.POST.get('patient_age') ,appointment_datetime= request.POST.get('appointment_datetime'),is_attended= request.POST.get('is_attended'))
        new_appointment.save()
    
    return redirect(request,"ClinicApp:view_doctor")#pro<<


def update_doctor(request: HttpRequest, doctor_id:int):
    pass
       