from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Doctor, Patient
from .serializers import DoctorSerializer, PatientSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer