from django.urls import path
from . import views 

app_name = "ClinicApp"

urlpatterns=[

    path("info/",views.homepage , name = "infoPage"),
    path("doctor/add", views.add_doctor,name = "add_doctor")

]