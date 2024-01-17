from django.shortcuts import render
from doctor.models import Doctor, Specialization


def home(request, specialization_slug=None):
    print("hi")
    doctors = Doctor.objects.all()
    specializations = Specialization.objects.all()
    print(specialization_slug)
    if specialization_slug is not None and specialization_slug != 'all':
        special = Specialization.objects.get(slug=specialization_slug)
        doctors = Doctor.objects.filter(specialization=special)
    return render(request, 'index.html', {'doctors': doctors, 'specializations': specializations})
