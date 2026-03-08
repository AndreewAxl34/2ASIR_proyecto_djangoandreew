from django.db import models

# Creacion del modelo de productos

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField(default=0)
    descripcion = models.TextField(blank=True, null=True)
    seccion = models.ForeignKey('secciones.Seccion', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre