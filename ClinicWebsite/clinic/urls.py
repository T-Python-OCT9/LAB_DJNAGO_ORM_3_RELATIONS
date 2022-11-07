from django.urls import path
from . import views



app_name = "clinic"


urlpatterns = [

    path("", views.home_page, name="home_page"),
    path("list/", views.list_doctors, name="list_doctors"),
    path("details/<doc_id>", views.detail_page, name="detail_page"),
    path("make/appointment/", views.make_appointment, name="make_appointment"),
    path("add/doctor/", views.add_doctor, name="add_doctor")


]