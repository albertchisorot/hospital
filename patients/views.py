from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Patient
from .forms import PatientForm, PatientIDForm
from django.db.models import Count
from datetime import timedelta, datetime


# View for adding a patient
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PatientForm()
    return render(request, 'patients/add_patient.html', {'form': form})

# View for retrieving a patient by patient number
def get_patient(request):
    patient = None
    if request.method == 'POST':
        form = PatientIDForm(request.POST)
        if form.is_valid():
            patient_number = form.cleaned_data['patient_number']
            try:
                patient = Patient.objects.get(patient_number=patient_number)
            except Patient.DoesNotExist:
                patient = None
    else:
        form = PatientIDForm()

    return render(request, 'patients/get_patient.html', {'form': form, 'patient': patient})

# View for displaying statistics
def patient_statistics(request):
    today = datetime.now().date()
    weekly = today - timedelta(weeks=1)
    monthly = today - timedelta(days=30)
    yearly = today - timedelta(days=365)

    statistics = {
        'daily': Patient.objects.filter(admission_date__date=today).count(),
        'weekly': Patient.objects.filter(admission_date__date__gte=weekly).count(),
        'monthly': Patient.objects.filter(admission_date__date__gte=monthly).count(),
        'yearly': Patient.objects.filter(admission_date__date__gte=yearly).count(),
    }

    return render(request, 'patients/statistics.html', {'statistics': statistics})

def dashboard(request):
    today = datetime.now().date()
    weekly = today - timedelta(weeks=1)
    monthly = today - timedelta(days=30)
    yearly = today - timedelta(days=365)

    statistics = {
        'daily': Patient.objects.filter(admission_date__date=today).count(),
        'weekly': Patient.objects.filter(admission_date__date__gte=weekly).count(),
        'monthly': Patient.objects.filter(admission_date__date__gte=monthly).count(),
        'yearly': Patient.objects.filter(admission_date__date__gte=yearly).count(),
    }

    return render(request, 'patients/dashboard.html', {'statistics': statistics})
