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
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    
    def __str__ (self):
        return self.nombre

class Incidencia(models.Model):
    TIPO = [
        ('electrica', 'Eléctrica'),
        ('limpieza','Limpieza'),
        ('mobiliario','Mobiliario'),
        ('climatizacion','Climatización')
    ]
    
    URGENCIA = [
        ('alta','Alta'),
        ('media','Media'),
        ('baja','Baja')    
    ]
    
    ESTADO = [
        ('abierta','Abierta'),
        ('en curso', 'En curso'),
        ('resuelta', 'Resuelta'),
        ('cancelada', 'Cancelada')
    ]
    
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=20, choices=TIPO)
    nivel_urgencia = models.CharField(max_length=10, choices=URGENCIA)
    estado = models.CharField(max_length=15, choices=ESTADO, default='Abierta')
    fecha_apertura = models.DateField(auto_now_add=True)
    fecha_resolucion = models.DateField(blank=True, null=True)     
    
    instalacion = models.ForeignKey(Instalacion, on_delete=models.CASCADE)
    empleado_aginado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    
    def __str__ (self):
        return self.titulo