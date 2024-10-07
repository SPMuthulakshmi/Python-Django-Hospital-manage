from django.urls import path
from . import views
from django.urls import path
from .views import add_doctor


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('patients/', views.patient_list, name='patient_list'),
    path('add-patient/', views.add_patient, name='add_patient'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('add-appointment/', views.add_appointment, name='add_appointment'),
    path('add-doctor/', views.add_doctor, name='add_doctor'),
]
