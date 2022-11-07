from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    experience_years = models.IntegerField()
    rating = models.FloatField()
    doctor_specialization = (
        ('GENERAL','General Doctor'),
        ('EMERGENCY','Emergency Doctor'),
        ('ORTHOPEDICS','Orthopedics Doctor'),
    )
    specialization = models.CharField(max_length=256, choices=doctor_specialization, default='GENERAL')
    image = models.ImageField(upload_to='images/')
        

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    case = models.TextField()
    age = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    attended = models.BooleanField(default=False)