from django.db import models
from patient.models import Patient
from doctor.models import Doctor


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    cancel = models.BooleanField(default=False)

    def __str__(self):
        return f"Doctor : {self.doctor.user.first_name} , Patient : {self.patient.user.first_name}"


class Review(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    comment = models.TextField()
