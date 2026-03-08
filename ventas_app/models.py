from django.db import models
from clientes.models import Cliente
from productos.models import Producto

# creacion del modelo de ventas_apps

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio_producto = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return f"Venta #{self.id} - {self.cliente.nombre}"
# esta parte del modelo nos servira para poder realizar el total del producto
    @property
    def total(self):
        return self.precio_producto * self.cantidad
