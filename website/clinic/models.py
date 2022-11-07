from django.db import models

# Create your models here.


    
    class Doctor(model.model):
    name= model.CharField(max_length=1024)
    description = models.TextField()
    specialization = models.DateTimeField()
    experience_years = models.ImageField(upload_to="image/")
rating
    class appointment(model.model):
    atient_name = model.CharField(max_length=1024)
    case_description = models.TextField()
    patient_age = models.DateTimeField()
    appointment_datetime = models.ImageField(upload_to="image/")
is_attended
    
### Models

- Doctor model should have
- - name
- - description
- - specialization (use text choices)
- - experience_years
- - rating



- Appointment Model
- - Relation with doctor
- - patient_name
- - case_description
- - patient_age
- - appointment_datetime
- - is_attended