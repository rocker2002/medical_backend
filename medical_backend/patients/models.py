from django.db import models
from django.contrib.auth.models import User
import uuid

class Doctor(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=256)
    specialization = models.CharField(max_length=256)
    email = models.EmailField(max_length=256, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.specialization}"

class Patient(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=256)
    date_of_birth = models.DateField()
    contact = models.CharField(max_length=256)
    my_doctor = models.ForeignKey(to=Doctor, on_delete=models.PROTECT, related_name='patients')

    def __str__(self):
        return f"{self.name} - {self.contact}"
    
class Profile(models.Model):
    class Roles(models.TextChoices):
        DOCTOR = 'DR', 'Doctor',
        PATIENT = 'PT', 'Patient',
        RECEPTIONIST = 'RT', 'Receptionist'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=Roles.choices)

    def __str__(self):
        return f"{self.user}"
