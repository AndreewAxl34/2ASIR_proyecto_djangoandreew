from django.shortcuts import render,redirect, get_object_or_404
from .models import Venta
from clientes.models import Cliente
from productos.models import Producto

# Creacion de las vistas
# para listar ventas
def listar_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas_app/listar.html',{'ventas': ventas})

# para crear ventas
def crear_ventas(request):
    clientes=Cliente.objects.all()
    productos=Producto.objects.all()
    
    if request.method == 'POST':
      cliente_id = request.POST['cliente']
      producto_id = request.POST['producto']
      cantidad = int(request.POST['cantidad'])
      producto=Producto.objects.get(id=producto_id)
      #Copiamos el precio del producto en el momento de laventa
      precio_producto=producto.precio

      Venta.objects.create(
          cliente_id=cliente_id,
          producto_id=producto_id,
          precio_producto=precio_producto,
          cantidad=cantidad
      )
      return redirect('listar_ventas')

    return render(request, 'ventas_app/crear.html', {
         'clientes':clientes,
         'productos':productos
    })
#para eliminar ventas
def eliminar_ventas(request, id):
   venta = get_object_or_404(Venta, id=id)
   
   if request.method == 'POST':
        venta.delete()
        return redirect('listar_ventas')
   
   return render(request, 'ventas_app/eliminar.html', {'venta':venta})
