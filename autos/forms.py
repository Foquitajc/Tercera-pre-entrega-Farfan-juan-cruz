# autos/forms.py

from django import forms
from .models import Marca, Auto

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre']

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ['marca', 'modelo', 'año']

