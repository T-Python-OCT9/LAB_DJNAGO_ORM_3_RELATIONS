from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    specialization = models.CharField(max_length=64)
    experience_years = models.CharField(max_length=64)
    rating = models.FloatField()



class Appointment(models.Model): 
    appointment = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    relation_with_doctor = models.CharField(max_length=256)
    pationt_name = models.CharField(max_length=64)
    case_description = models.TextField()
    patient_age = models.CharField(max_length=64)
    appointment_datetime = models.DateTimeField()
    is_attended = models.BooleanField()

