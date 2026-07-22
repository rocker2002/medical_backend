from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsDoctor
from .models import Doctor, Patient, Appointment
from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer
from django_filters.rest_framework import DjangoFilterBackend

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.select_related('my_doctor').all()
    serializer_class = PatientSerializer
    permission_classes = [IsDoctor]

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.select_related('doctor', 'patient').all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'doctor']