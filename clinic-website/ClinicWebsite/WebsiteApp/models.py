from django.db import models

# Create your models here.

class Doctor(models.Model):
   
    
    Docname = models.CharField(max_length=256)
    DocDescrip = models.TextField()
    DocRate = models.FloatField()
    experience_years = models.IntegerField()
    DocSpecialization = models.CharField(max_length=256)
    
   

class Patient(models.Model):
    Relation_with_doctor=models.ForeignKey(Doctor , on_delete=models.CASCADE)
    p_name = models.CharField(max_length=256)
    case_description = models.TextField()
    p_age = models.IntegerField()
    Appointment_datetime = models.DateTimeField(auto_now=True)
    is_attend=models.BooleanField()




