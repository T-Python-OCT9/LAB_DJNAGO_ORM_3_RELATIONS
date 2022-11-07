from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Doctor, Appointment
# Create your views here.

def home(request:HttpRequest):
    return render(request, 'base.html')


def add_doctor(request : HttpRequest):

    if request.method == "POST":
        new_doctor = Doctor(name=request.POST["name"], description = request.POST["description"], specialization=request.POST["specialization"], experience_years = request.POST["experience_years"], rating = request.POST["rating"])
        new_doctor.save()


    return render(request, "add_doctor.html")



def view_doctor(request: HttpRequest):
    doctor = Doctor.objects.all()
    #posts = Post.objects.all().order_by("-publish_date") #to order by date
    #posts = Post.objects.filter(is_published=False) #to filter by exact
    #posts = Post.objects.filter(title__contains = "aims") #to filter using postfix __contains
    return render(request, "view_doctor.html", {"doctor" : doctor})


def doctor_detail(request : HttpRequest, post_id : int):

    try:
        doctor = Doctor.objects.get(id=post_id)
    except:
        return render(request , "not_found.html")

    return render(request, "doctor_detail.html", {"details" : doctor})

def update_doctor(request: HttpRequest, post_id:int):

    try:
        doctor = Doctor.objects.get(id=post_id)
    except:
        return render(request , "not_found.html")

    if request.method == "POST":
        Doctor.name = request.POST["name"]
        Doctor.description = request.POST["description"]
        Doctor.specialization = request.POST["specialization"]
        Doctor.experience_years = request.POST["experience_years"]
        Doctor.rating = request.POST["rating"]
        Doctor.save()

        return redirect("clinic:view_doctor")

    


#delete post
def delete_doctor(request: HttpRequest, post_id:int):

    try:
        doctor = Doctor.objects.get(id=post_id)
    except:
        return render(request , "not_found.html")

    doctor.delete()

    return redirect("clinic:view_doctor")