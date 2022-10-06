from django import forms

class CrearListaForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
