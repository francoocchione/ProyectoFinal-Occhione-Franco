from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Articulos(models.Model):
    titulo = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=150)
    contenido = RichTextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articulos_creados') 
    fecha = models.DateTimeField()
    foto = models.ImageField(upload_to='images/', blank = True, null = True)
    
    def save(self, *args, **kwargs):
        if not self.id:  # If the instance is being created for the first time
            from django.utils import timezone
            self.fecha = timezone.now()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.titulo}, {self.subtitulo}, {self.contenido}"
    
class Aves(models.Model):
    orden = models.CharField(max_length=200)
    familia = models.CharField(max_length=200)
    especie = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    caracteristicas = models.TextField()
    ultima_observacion = models.DateField()
    foto = models.ImageField(upload_to='images/', blank = True, null = True)
    audio = models.FileField(upload_to='audio/', blank = True, null = True)
    
    def __str__(self):
        return f"{self.nombre} - {self.especie}"