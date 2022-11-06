from django.shortcuts import render,redirect
from django.http import HttpRequest
from.models import Doctor,Appointment





#____________________________________________

#home


def home(request:HttpRequest):

    return render(request,'clinicApp/clinic.html')


#____________________________________________

#add doctors data

def addDoctor(request:HttpRequest):
    if request.method == "POST":
        doctor_form=Doctor(name=request.POST["name"],description=request.POST["description"],experience_years=request.POST["experience_years"],rating=6.0)
        doctor_form.save()
    return render(request,'clinicApp/doctorAdd.html')

#____________________________________________

#add appointment data


def addAppointment(request:HttpRequest,post_id:int):
    doctor = Doctor.objects.get(id=post_id)
    if request.method == "POST":
        appointment_form=Appointment(patient_name=request.POST["patient_name"],case_description=request.POST["case_description"],patient_age=request.POST["patient_age"],appointment_datetime=request.POST["appointment_datetime"],is_attended=request.POST["is_attended"])
        appointment_form.save()
    return redirect('clinicApp:views',doctor.id)

#____________________________________________

#doctor view data

def postDoctor(request:HttpRequest):
    if "search" in request.GET:
        doctor=Doctor.objects.filter(name__contains = request.GET["search"])
    else:
        doctor=Doctor.objects.all()
    return render(request,'clinicApp/post_d.html',{"docor_p":doctor})

#____________________________________________

#view

def view_info(request:HttpRequest,post_id : int):
    doctor=Doctor.objects.get(id=post_id)
    appointment_info=Appointment.objects.filter(doctor=doctor)
    return render(request,'clinicApp/viewsDoctor.html',{"postView":doctor,"app_info":appointment_info})


#____________________________________________

#appointment view data

#def poAppo(request:HttpRequest):
    #appointment=Appointment.objects.all()
    #return render(request,'clinicApp/post_appo.html',{"appo_post":appointment})







