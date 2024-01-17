from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    user = models.OneToOneField(
        User, related_name="patient", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="patient/images/")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
