from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import DoctorForm, PatientForm, AppointmentForm, PrescriptionForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Doctor, Appointment
from .forms import AppointmentForm  

# Add Doctor View
def add_doctor(request):
    from .models import Doctor 

    if request.method == 'POST':
        username = request.POST.get('user')  # Username input
        first_name = request.POST.get('first_name')  
        last_name = request.POST.get('last_name')  
        specialization = request.POST.get('specialization')  
        contact_number = request.POST.get('contact_number') 

        if User.objects.filter(username=username).exists():
            return render(request, 'add_doctor.html', {'error': 'User already exists.'})

        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name)
        
        doctor = Doctor.objects.create(user=user, specialization=specialization, contact_number=contact_number)
        doctor.save()
        
        return redirect('doctor_list')  
    else:
        return render(request, 'add_doctor.html')

def dashboard(request):
    from .models import Doctor, Patient, Appointment  
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    appointments = Appointment.objects.all()
    context = {
        'doctors': doctors,
        'patients': patients,
        'appointments': appointments,
    }
    return render(request, 'dashboard.html', context)

# List Doctors
def doctor_list(request):
    from .models import Doctor  
    doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})

# Add Patient
def add_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'add_patient.html', {'form': form})

# List Patients
def patient_list(request):
    from .models import Patient  
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})

def add_appointment(request):
    doctors = Doctor.objects.all()  
    if request.method == 'POST':
        doctor_id = request.POST.get('doctor')
        patient_name = request.POST.get('patient_name')  # This should be the text input field
        appointment_date = request.POST.get('appointment_date')
        symptoms = request.POST.get('symptoms')

        appointment = Appointment.objects.create(
            doctor_id=doctor_id,
            patient_name=patient_name,
            appointment_date=appointment_date,
            symptoms=symptoms
        )
        messages.success(request, "Appointment added successfully!") 
        return redirect('appointment_list')  # Make sure this redirects to the appointment list
    return render(request, 'add_appointment.html', {'doctors': doctors})


# List Appointments
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment_list.html', {'appointments': appointments})
