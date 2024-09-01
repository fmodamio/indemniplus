from django import forms
from .models import DatosFormulario

class DatosFormularioForm(forms.ModelForm):
    class Meta:
        model = DatosFormulario
        fields = ['nombre', 'telefono', 'email', 'mensaje']
