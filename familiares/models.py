from django.db import models

# Create your models here.

class familiares(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.CharField(max_length=10)
    fecha = models.DateField(max_length=10)