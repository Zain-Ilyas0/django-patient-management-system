from django.db import models

# Create your models here.

class PatientData(models.Model):
    patient_name = models.CharField(max_length=100)
    patient_number = models.IntegerField()
    patient_issue = models.CharField(max_length=200)
    appointment_date = models.DateTimeField()

    is_deleted = models.BooleanField(default=False)


    def __str__(self):
        return self.patient_name
    