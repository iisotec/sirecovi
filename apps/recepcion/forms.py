from django import forms
from .models import Visitante, VisitanteOficina

class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        exclude = ('views','created','modified',)
        widgets = {
            'dni': forms.TextInput(attrs={'class': 'form-control', 'autocomplete':'off'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'rows': '2'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'rows': '2'}),
            'oficinas' : forms.SelectMultiple(attrs={'class': 'form-control', 'rows': '3'}),
             }
class VisitanteOficinaForm(forms.ModelForm):
    class Meta:
        model = VisitanteOficina
        exclude = ('views','created','modified',)
        widgets = {
            'oficina': forms.Select(attrs={'class': 'form-control', 'autocomplete':'off'}),
            'visitante': forms.Select(attrs={'class': 'form-control', 'rows': '2'}),
             }