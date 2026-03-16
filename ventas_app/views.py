from django.shortcuts import render,redirect, get_object_or_404
from .models import Venta
from clientes.models import Cliente
from productos.models import Producto

# Creacion de las vistas
# para listar ventas
def listar_ventas(request):
    #)1 empezamos mostrando todas las ventas
    ventas = Venta.objects.all()

     #2) Recogemos lo que hay en el formulario (si es que lo hay)
    desde = request.GET.get("desde")
    hasta = request.GET.get("hasta")
    
    #3) Si el usuariio ha puesto una fecha desde , filtramos a paritr de esa fecha
    if desde:
       ventas = ventas.filter(fecha__gte=desde)
 
    #4) Si el usuariio ha puesto una fecha hasta , filtramos a paritr de esa fecha
    if hasta:
       ventas = ventas.filter(fecha__lte=hasta)

    #Contar ventas filtradas
    total_ventas=ventas.count()
 
    return render(request, 'ventas_app/listar.html',{
        'ventas': ventas,
        'desde': desde,
        'hasta': hasta,
        'total_ventas': total_ventas
        })

# para crear ventas
def crear_ventas(request):
    clientes=Cliente.objects.all()
    productos=Producto.objects.all()
    
    if request.method == 'POST':
      cliente_id = request.POST['cliente']
      producto_id = request.POST['producto']
      cantidad = int(request.POST['cantidad'])
      fecha = request.POST['fecha']
      producto=Producto.objects.get(id=producto_id)
      #Copiamos el precio del producto en el momento de laventa
      precio_producto=producto.precio

      Venta.objects.create(
          cliente_id=cliente_id,
          producto_id=producto_id,
          precio_producto=precio_producto,
          cantidad=cantidad,
          fecha=fecha
      )
      return redirect('listar_ventas')

    return render(request, 'ventas_app/crear.html', {
         'clientes':clientes,
         'productos':productos
    })

def editar_ventas(request, id):
    ventas = get_object_or_404(Venta, id=id)
    clientes=Cliente.objects.all()
    productos=Producto.objects.all()

    if request.method == 'POST':
        ventas.cliente_id = request.POST.get('cliente')
        ventas.producto_id = request.POST.get('producto')
        ventas.cantidad = request.POST.get('cantidad')
        ventas.fecha = request.POST.get('fecha')
        ventas.save()

        return redirect('listar_ventas')

    return render(request, 'ventas_app/editar.html', {
        'ventas_app': ventas,
        'clientes': clientes,
        'productos': productos
    })


#para eliminar ventas
def eliminar_ventas(request, id):
   venta = get_object_or_404(Venta, id=id)
   
   if request.method == 'POST':
        venta.delete()
        return redirect('listar_ventas')
   
   return render(request, 'ventas_app/eliminar.html', {'venta':venta})
