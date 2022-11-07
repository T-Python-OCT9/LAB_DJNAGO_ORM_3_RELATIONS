from django.urls import path
from . import views

app_name = "clinic"

urlpatterns = [
    path("doctor/add/", views.add_doctor, name="add_doctor"),
    
]