from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)

from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    contact_number = models.CharField(max_length=20)
    address = models.TextField()
    medical_history = models.TextField(blank=True, null=True)  # Optional field

    def __str__(self):
        return self.name


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=255)  # If you're using a text field for the patient's name
    appointment_date = models.DateField()
    symptoms = models.TextField()

# Prescription model
class Prescription(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    details = models.TextField()

    def __str__(self):
        return f"Prescription for {self.appointment.patient.name}"
