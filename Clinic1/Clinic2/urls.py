from django.urls import path
from . import views

app_name = "Clinic2"

urlpatterns = [
    path("Home/", views.Home, name="Home"),
    path("det/", views.detail, name="detail"),
    path("search/", views.search, name="search"),
   
]