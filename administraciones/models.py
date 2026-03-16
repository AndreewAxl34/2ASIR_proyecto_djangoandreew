from django.db import models


# Creacion de modelo de administacion
class Administracion(models.Model):
    nombre = models.CharField(max_length=100)
    sector_industrial = models.CharField(max_length=100)
    domicilio = models.TextField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    numero_empleados = models.IntegerField(default=0)
    estructura_organizativa = models.CharField(max_length=100)
    tipo_iva =  models.DecimalField(max_digits=5, decimal_places=2,default=21.00)
    socios = models.CharField(max_length=100)

    def __str__(self):
      return self.nombre

