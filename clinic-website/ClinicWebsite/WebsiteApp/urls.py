from django.urls import path
from . import views

app_name = "WebsiteApp"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("gallary/",views.gallary,name="gallary"),
    path("add_doctor/",views.add_doctor,name="add_doctor"),
     path("detail/",views.doctor_list,name="doctor_list")


]