from django.urls import path
from . import views


app_name = 'clinic'

urlpatterns = [
    path('', views.homePage, name='home'),
    path('doctors/', views.getDoctors, name='doctors'),
       path('search/', views.searchDoctor, name='search'),
       path('doctors/add/', views.addDoctor, name='add'),
       path('doctors/remove/<int:doctor_id>/', views.removeDoctor, name='remove'),
       path('doctor/update/<int:doctor_id>/', views.updateDoctor, name='update'),

]