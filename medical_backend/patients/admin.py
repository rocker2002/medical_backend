from django.contrib import admin
from .models import Doctor, Patient, Profile, Appointment

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Profile)
admin.site.register(Appointment)

