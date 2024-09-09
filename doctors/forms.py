from .models import *
from django import forms


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'specializes', 'phone', 'is_active']
