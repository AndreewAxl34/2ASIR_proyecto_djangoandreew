from django.shortcuts import render,redirect, get_object_or_404
from .models import Producto
from secciones.models import Seccion

# Creacion de las vistas
# para listar productos
def listar_productos(request):
    productos= Producto.objects.all()
    return render(request, 'productos/listar.html', {'productos' : productos})
# para crear productos
def crear_productos(request):
    secciones = Seccion.objects.all()

    if request.method == 'POST':
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        stock = request.POST['stock']
        descripcion = request.POST['descripcion']
        seccion_id = request.POST['seccion']

        Producto.objects.create(
            nombre=nombre,
            precio=precio,
            stock=stock,
            descripcion=descripcion,
            seccion_id=seccion_id
        )
        return redirect('listar_productos')
    
    return render(request, 'productos/crear.html', {
         'secciones': secciones
    })
# para editar productos
def editar_productos(request, id):
     producto = get_object_or_404(Producto, id=id)
     secciones = Seccion.objects.all()

     if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.precio = request.POST['precio']
        producto.stock = request.POST['stock']
        producto.descripcion = request.POST['descripcion']
        producto.seccion_id = request.POST['seccion']
        producto.save()
        return redirect('listar_productos')

     return render(request, 'productos/editar.html', {
        'producto': producto,
        'secciones': secciones
    })
# para elimintar productos
def eliminar_productos(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')

    return render(request, 'productos/eliminar.html',{
        'producto': producto
    })

