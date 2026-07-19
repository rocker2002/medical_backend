from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Doctor, Patient
from .serializers import DoctorSerializer, PatientSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    doctor = Doctor.objects.all()
    serializer = DoctorSerializer

class PatientViewSet(viewsets.ModelViewSet):
    patient = Patient.objects.all()
    serializer = PatientSerializer