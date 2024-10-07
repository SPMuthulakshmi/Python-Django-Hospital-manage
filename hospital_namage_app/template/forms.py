from django import forms
from django.contrib.auth.models import User
from .models import Doctor, Patient, Appointment, Prescription
from .models import Appointment, Doctor  # Importing models
class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['user', 'specialization', 'contact_number']

from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'contact_number', 'address', 'medical_history']
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'patient_name', 'appointment_date', 'symptoms'] 

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['appointment', 'details']
