import xml.etree.ElementTree as ET
from django.db import models
from datetime import datetime

class Patient(models.Model):
    patient_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    admission_date = models.DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Save data to XML
        self.save_to_xml()

    def save_to_xml(self):
        root = self.load_xml()
        patient_data = ET.Element('patient')
        ET.SubElement(patient_data, 'patient_number').text = self.patient_number
        ET.SubElement(patient_data, 'name').text = self.name
        ET.SubElement(patient_data, 'age').text = str(self.age)
        ET.SubElement(patient_data, 'gender').text = self.gender
        ET.SubElement(patient_data, 'address').text = self.address
        ET.SubElement(patient_data, 'phone_number').text = self.phone_number
        ET.SubElement(patient_data, 'admission_date').text = self.admission_date.strftime('%Y-%m-%d %H:%M:%S')

        root.append(patient_data)
        tree = ET.ElementTree(root)
        tree.write('patients_data.xml')

    @staticmethod
    def load_xml():
        try:
            tree = ET.parse('patients_data.xml')
            return tree.getroot()
        except FileNotFoundError:
            root = ET.Element('patients')
            return root

    def __str__(self):
        return f"{self.name} - {self.patient_number}"
