from django.db import models
from django.utils import timezone
# Create your models here.

class ubicaciones(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    cultivo = models.CharField(max_length=100)
    municipio  = models.CharField(max_length=100)
    cedula  = models.CharField(max_length=100)
    telefono  = models.CharField(max_length=100)
    email  = models.CharField(max_length=100)
    tipo  = models.CharField(max_length=100)

