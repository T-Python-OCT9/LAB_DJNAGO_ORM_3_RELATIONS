from django.db import models

# Create your models here.

specialization_choices = ("Dentist", "Dermatologist","Optometrist", )

class doctor (models.Model):
    name = models.CharField(max_length=512)
    description = models.TextField()
    specialization = specialization_choices
    experience_years = models.IntegerField()
    rating= models.FloatField()

'''
class Appointment(models.Model):
    doctor = models.ManyToManyField(doctor, on_delete= models.CASCADE )
    patient_name = models.CharField(max_length=512)
    case_description = models.CharField(max_length=512)
    patient_age= models.IntegerField()
    appointment_datetime = models.DateTimeField()
    is_attended = models.BooleanField()

'''
   