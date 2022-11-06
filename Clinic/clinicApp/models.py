from django.db import models


class Doctor(models.Model):
    name=models.CharField(max_length=256)
    description=models.TextField()
    specialization=models.TextField()
    experience_years=models.CharField(max_length=256)
    rating=models.FloatField()

class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient_name=models.CharField(max_length=256)
    case_description=models.TextField()
    patient_age=models.CharField(max_length=256)
    appointment_datetime=models.DateTimeField()
    is_attended=models.BooleanField()
# Create your models here.
