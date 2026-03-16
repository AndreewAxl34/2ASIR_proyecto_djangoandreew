from django.db import models

# creacion del modelo de cliente

class Cliente(models.Model):
    nombre= models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_registro= models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now=True)

    class Meta:
  #      ordering = ['nombre'] # Se encarga de ordenar nombres por el alfabeto
     verbose_name = "Cliente" # Nombre en el admin
     verbose_name_plural = "Clientes" # Nombre prural en el admin

    def __str__(self):
        return f"{self.nombre} ({self.email})"
