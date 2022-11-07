from django.db import models



# Create your models here.


class Doctor(models.Model):
    #specialization_choices = models.TextChoices("Specialization", ["Orthopedica", "Pediatrics"])

    name = models.CharField(max_length = 256)
    desc = models.TextField()
    #specialization = models.CharField(max_length=64, choices=specialization_choices.choices)
    experience = models.IntegerField()
    rating = models.FloatField()


class Appointment(models.Model):

    relation_with_d = models.CharField(max_length= 256)
    patient_name = models.CharField(max_length= 256)
    case_desc = models.TextField()
    patient_age = models.IntegerField()
    appointment_datetime = models.DateTimeField(auto_now=True)
    is_attended = models.BooleanField()


