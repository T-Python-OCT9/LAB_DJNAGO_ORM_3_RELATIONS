from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length = 256)
    description = models.TextField()
    spec_choices = models.TextChoices('specialization' , 'FamilyMedicine Surgery Anesthesiology Physiotherapy Dental' )
    SPECIALIZATION_CHOICES = [
        ("FAMILYMEDICINE", 'Family medicine'),
        ("SURGERY", 'Surgery'),
        ("ANESTHESIOLOGY", 'Anesthesiology'),
        ("PHSIOTHERAPY",'Physiotherapy'),
        ("DENTAL",'Dental')
    ]
    specialization = models.CharField(
        max_length=256,
        choices= spec_choices.choices,
        default=SPECIALIZATION_CHOICES[0][0],
    )
    experience_years = models.IntegerField()
    rating = models.FloatField()


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor , on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=256)
    case_description = models.TextField()
    patient_age = models.IntegerField()
    appointment_datetime = models.DateTimeField()
    is_attended =models.BooleanField()