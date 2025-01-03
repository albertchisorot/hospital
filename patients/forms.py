from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['patient_number', 'name', 'age', 'gender', 'address', 'phone_number']

class PatientIDForm(forms.Form):
    patient_number = forms.CharField(max_length=20)
