from django import forms
from apps.oficina.models import Oficina
from apps.recepcion.models import Visitante
from apps.users.models import User

class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        exclude = ('views','created','modified',)
        widgets = {
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'rows': '2'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'rows': '2'}),
            'oficina' : forms.SelectMultiple(attrs={'size':'8','class': 'form-control'}),
             }

class OficinaForm(forms.ModelForm):
    class Meta:
        model = Oficina
        exclude = ('views','created','modified',)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'estado_oficina': forms.CheckboxInput(),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
       		 }
 #ModelChoiceField(queryset=YourModel.objects.all()),
  #                                           empty_label="Choose a countries",)