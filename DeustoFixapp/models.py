from django.db import models

class Instalacion(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    tipo_uso = models.CharField(max_length=50, blank=True)
    ubiacion = models.CharField(max_length=100)
    capacidad =  models.IntegerField(null=True, blank=True)
    estado = models.CharField(max_length=20, default='Activa')
    departamento_responsable = models.CharField(max_length=100)
    
    def __str__ (self):
        return self.nombre
    
class Empleado(models.Model):
    dni = models.CharField(max_length=9, unique=True)
    
