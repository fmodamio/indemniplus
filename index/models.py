from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class DatosFormulario(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = PhoneNumberField(region="ES",error_messages={'invalid': 'Por favor, introduce un número de teléfono válido.'})
    email = models.EmailField()
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return self.nombre
