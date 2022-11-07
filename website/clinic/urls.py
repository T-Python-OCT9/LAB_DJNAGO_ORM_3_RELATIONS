from django.urls import path
from . import views
app_name= "clinic"
urlpatterns=[
    path("home/", views.home, name="home"),
    path("details/",views.detailPage,name="details"),
    path("book/",views.bookingpage,name="book"),
    
]