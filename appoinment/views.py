from django.shortcuts import render, redirect
from doctor.models import Doctor
from patient.models import Patient
from .models import Appointment


def book_appointment(request, doctor_id):
    doctor = Doctor.objects.get(pk=doctor_id)
    user = request.user

    patient, created = Patient.objects.get_or_create(user=user)
    Appointment.objects.create(
        doctor=doctor,
        patient=patient
    )

    return redirect(f"/doctor/detail/{doctor_id}/")


def delete_patient(request, doctor_id, patient_id):
    doctor = Doctor.objects.get(pk=doctor_id)
    patient = Patient.objects.get(pk=patient_id)
    appointment = Appointment.objects.filter(
        doctor=doctor,
        patient=patient
    )
    if appointment.exists():
        appointment.delete()
        return redirect('profile')
    else:
        return redirect('profile')
