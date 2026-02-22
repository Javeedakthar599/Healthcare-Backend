
from django.db import models
from patients.models import Patient
from doctors.models import Doctor

class Mapping(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
