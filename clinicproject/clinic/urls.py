from django.urls import path
from . import views

app_name = "clinic"

urlpatterns = [ 
    path("", views.home, name="home"), 
    path("add_doctor", views.add_doctor, name="add_doctors"), 
    path("doctors/", views.doctors, name="list_doctors"),
    path("view/<int:doctor_id>/", views.view_doctor, name="view_doctor"), 

    path("view/<int:doctor_id>/appointment/", views.appointment, name="appointment"),
    
    path("add_appointment/<int:doctor_id>/", views.add_appointment, name="add_appointment"),

]