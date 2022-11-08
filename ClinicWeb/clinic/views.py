from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import Doctor


# Create your views here.
def homePage(request: HttpRequest):
    doctors = Doctor.objects.all()[:4]
    context = {'doctors':doctors}
    return render(request, 'clinic/home.html', context)


def getDoctors(request: HttpRequest):
    doctors = Doctor.objects.all()
    context = {'doctors':doctors}
    return render(request, 'clinic/list.html', context)

def addDoctor(request: HttpRequest):
    doctor_specializations = Doctor.specialization_choices.choices
    if request.method == 'POST':
        doctor = Doctor(name=request.POST['name'], description=request.POST['description'], experience_years=request.POST['experience_years'], rating=request.POST['rating'], specialization=request.POST['specialization'], image=request.FILES['image'])
        doctor.save()
        return redirect('clinic:doctors')
    context = {'doctor_specializations':doctor_specializations}
    return render(request, 'clinic/add.html', context)

def searchDoctor(request: HttpRequest):
    doctors = Doctor.objects.all().filter(name__contains=request.GET.get('doctor', ''))
    context = {'doctors':doctors}
    return render(request, 'clinic/search.html', context)


def removeDoctor(request: HttpRequest, doctor_id: int):
    try:
        doctor = Doctor.objects.get(id=doctor_id)
        doctor.delete()
        return redirect('clinic:doctors')
    except:
        return render(request, 'clinic/not_found.html')



def updateDoctor(request: HttpRequest, doctor_id: int):
    pass
    return render(request, 'clinic/update.html')

