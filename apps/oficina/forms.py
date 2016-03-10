from django import forms
from .models import Oficina


class OficinaForm(forms.ModelForm):
    class Meta:
        model = Oficina
        exclude = ('views','created','modified',)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(),
            'visit_oficina': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
             }
 #ModelChoiceField(queryset=YourModel.objects.all()),
  #                                           empty_label="Choose a countries",)