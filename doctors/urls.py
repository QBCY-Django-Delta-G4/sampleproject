from django.urls import path
from .views import create_doctor

urlpatterns = [
    path('createdoctor/', create_doctor, name='create_view'),
]