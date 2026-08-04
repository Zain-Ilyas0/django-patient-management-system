from rest_framework import serializers
from .models import PatientData

class PatientDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientData
        fields = ["id", "patient_name", "patient_number", "patient_issue", "appointment_date", "is_deleted"]
        