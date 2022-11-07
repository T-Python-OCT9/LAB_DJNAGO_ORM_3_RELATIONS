from django.urls import path
from . import views

app_name = "clinic"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("view/", views.view_doctor, name="view_doctor"),
    path("add/", views.add_doctor, name="add_doctor"),
    path("Doctor/detail/<post_id>/", views.doctor_detail, name="doctor_detail"),
    path("post/update/<post_id>/", views.update_doctor, name="update_post"),
    path("post/delete/<post_id>/", views.delete_doctor, name="delete_post"),
]