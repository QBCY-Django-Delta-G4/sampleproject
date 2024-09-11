from django.shortcuts import render
from .forms import *


def create_doctor(request):
    if request.method =='POST':
        forms = DoctorForm(request.POST)
        if not forms.is_valid():
            return render(request, 'create_doctor.html', {'forms': forms})
        forms.save()
    else:
        forms = DoctorForm()
        return render(request, 'create_doctor.html', {'forms': forms})


def add_doctor(request):
    if request.method =='POST':
        forms = DoctorForm(request.POST)
        if not forms.is_valid():
            return render(request, 'create_doctor.html', {'forms': forms})
        forms.save()
    else:
        print('test')
        forms = DoctorForm()
        return render(request, 'create_doctor.html', {'forms': forms})
