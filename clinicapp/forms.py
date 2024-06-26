from django import forms
from django.core import validators
from clinicapp.models import ClinicalData, Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"

class ClinicalDataForm(forms.ModelForm):
    class Meta:
        model = ClinicalData
        fields = "__all__"



