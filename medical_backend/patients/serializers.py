from .models import Doctor, Patient, Appointment
from rest_framework import serializers
from django.utils import timezone

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
    def validate_scheduled_time(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Date and Time must be current or later")
        return value
    
    def validate(self, data):
        query = Appointment.objects.filter(doctor=data.get('doctor'), scheduled_time=data.get('scheduled_time'))
        if self.instance != None:
            query = query.exclude(id=self.instance.id)
        if query.exists():
            raise serializers.ValidationError("Doctor cannot have two appointment at the same time.")
        return data