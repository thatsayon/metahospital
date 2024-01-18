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
