from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Doctor, Appointment
from .doctors import Doctors
# Create your views here. 

doctor1 = Doctors("Ahmad", "Doctor specializing in Neurology", "Nerves",10 , 5)
doctor2 = Doctors("Sara", "Specialized in skin diseases and the conduct of surgical and non-surgical operations", "Skin diseases",7 , 5)
doctor3 = Doctors("Nora", "Diagnosis and treatment of childhood diseases", "Pediatric",7 , 4)
doctor4 = Doctors("Mohamad", "Specialist in Psychiatry", "Psychiatric illness",6 , 4)

list = [doctor1, doctor2, doctor3, doctor4]



def Home(request : HttpRequest):
    
    limit = int(request.GET.get("limit", 5))

    output = " "

    for doc in list[:limit]:
        output += doc.getName()
        
        
    return render(request, "Clinic2/Home.html",{"list" : output})






def detail(request : HttpRequest):

    context = {
        "doctor1" :  ["Ahmad", "Doctor specializing in Neurology", "Nerves", 10, 5] , 
        "doctor2": ["Sara", "Specialized in skin diseases and the conduct of surgical and non-surgical operations", "Skin diseases", 7, 5],
        "doctor3" : ["Nora", "Diagnosis and treatment of childhood diseases", "Pediatric", 7, 4],
        "doctor4" : ["Mohamad", "Specialist in Psychiatry", "Psychiatric illness", 6, 4],
        }

    return render(request, "Clinic2/detail.html", context )


def search(request : HttpRequest):

    pass