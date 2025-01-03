from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_patient, name='add_patient'),
    path('get/', views.get_patient, name='get_patient'),
    path('statistics/', views.patient_statistics, name='patient_statistics'),
]
