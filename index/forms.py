from django import forms
from .models import DatosFormulario
from django.core.exceptions import ValidationError

class DatosFormularioForm(forms.ModelForm):

    aceptar_terminos = forms.BooleanField(
        required=True,
        label="Estoy de acuerdo con el tratamiento de mis datos personales",
        error_messages={
            'required': 'Debes aceptar el tratamiento de datos personales para poder enviar tu caso.'
        }
    )

    class Meta:
        model = DatosFormulario
        fields = ['nombre', 'telefono', 'email', 'mensaje', 'aceptar_terminos']
