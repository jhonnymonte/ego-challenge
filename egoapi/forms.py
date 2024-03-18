from django import forms
from django.forms import CheckboxSelectMultiple
from .models import Vehiculo

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'
        widgets = {
            'colores': CheckboxSelectMultiple(),
        }
