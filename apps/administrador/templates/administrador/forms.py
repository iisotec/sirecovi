from django import forms
from .models import Visitante

class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        exclude = ('views','created','modified',)
        widgets = {
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'rows': '2'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'rows': '2'}),
            'fecha_visita': forms.DateTimeInput(attrs={'class': 'form-control'}),
            }