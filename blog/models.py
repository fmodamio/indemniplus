# blog/models.py
from django.db import models

class Entrada(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
