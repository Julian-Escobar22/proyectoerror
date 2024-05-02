from django.db import models

# Create your models here.
class contenido(models.Model):
    nombre=models.CharField(max_length=20)
    genero=models.CharField(max_length=20)
    duracion=models.IntegerField()
    descripcion=models.CharField(max_length=100)
    actores=models.CharField(max_length=40)
    director=models.CharField(max_length=40)
