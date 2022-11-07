from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Doctor, Appointment
from datetime import datetime

# Create your views here.
def homePage(request: HttpRequest):
    doctors = Doctor.objects.all()[:4]
    context = {'doctors':doctors}
    return render(request, 'clinic/home.html', context)

def getDoctors(request: HttpRequest):
    doctors = Doctor.objects.all()
    for doctor in doctors:
        for specialize in doctor.doctor_specialization:
            if doctor.specialization == specialize[0]:
                doctor.specialization = specialize[1]
    context = {'doctors':doctors}
    return render(request, 'clinic/list.html', context)

def addDoctor(request: HttpRequest):
    doctor_specializations = Doctor.doctor_specialization
    if request.method == 'POST':
        doctor = Doctor(name=request.POST['name'], description=request.POST['description'], experience_years=request.POST['experience_years'], rating=request.POST['rating'], specialization=request.POST['specialization'], image=request.FILES['image'])
        doctor.save()
        return redirect('clinic:doctors')
    context = {'doctor_specializations':doctor_specializations}
    return render(request, 'clinic/add.html', context)

def updateDoctor(request: HttpRequest, doctor_id: int):
    try:
        doctor = Doctor.objects.get(id=doctor_id)
        doctor_specializations = Doctor.doctor_specialization
        if request.method == 'POST':
            doctor.name = request.POST['name']
            doctor.description = request.POST['description']
            doctor.experience_years = request.POST['experience_years']
            doctor.rating = request.POST['rating']
            doctor.specialization = request.POST['specialization']
            doctor.image = request.FILES['image']
            doctor.save()
            return redirect('clinic:doctors')
    except:
        return render(request, 'clinic/not_found.html')
    context = {'doctor_specializations':doctor_specializations, 'doctor':doctor}
    return render(request, 'clinic/update.html', context)

def removeDoctor(request: HttpRequest, doctor_id: int):
    try:
        doctor = Doctor.objects.get(id=doctor_id)
        doctor.delete()
        return redirect('clinic:doctors')
    except:
        return render(request, 'clinic/not_found.html')

def doctorDetail(request: HttpRequest, doctor_id: int):
    try:
        doctor = Doctor.objects.get(id=doctor_id)
        appointments = Appointment.objects.filter(doctor=doctor)
        for specialize in Doctor.doctor_specialization:
            if doctor.specialization == specialize[0]:
                doctor.specialization = specialize[1]
    except:
        return render(request, 'clinic/not_found.html')
    context = {'doctor':doctor, 'appointments':appointments}
    return render(request, 'clinic/detail.html', context)

def bookAppointment(request: HttpRequest, doctor_id: int):
    try:
        doctor = Doctor.objects.get(id=doctor_id)
        if request.method == 'POST':
            new_appointment = Appointment(doctor=doctor, name=request.POST['name'], case=request.POST['case'], age=request.POST['age'])
            new_appointment.save()
    except:
        return render(request, 'clinic/not_found.html')
    return redirect('clinic:detail', doctor.id)

def searchDoctor(request: HttpRequest):
    doctors = Doctor.objects.all().filter(name__contains=request.GET.get('doctor', ''))
    for doctor in doctors:
        for specialize in doctor.doctor_specialization:
            if doctor.specialization == specialize[0]:
                doctor.specialization = specialize[1]
    context = {'doctors':doctors}
    return render(request, 'clinic/search.html', context)

def galleryPage(request: HttpRequest):
    context = {}
    return render(request, 'clinic/gallery.html', context)

