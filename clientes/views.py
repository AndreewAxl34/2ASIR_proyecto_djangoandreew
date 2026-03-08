from django.shortcuts import render,redirect, get_object_or_404
from .models import Cliente

# Creacion del as vistas de clientes
#Vista para listar clientes
def listar_clientes(request):
    clientes= Cliente.objects.all()
    return render(request, 'clientes/listar.html', {
        'clientes': clientes
    })

#Vista para crear clientes
def crear_clientes(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        telefono = request.POST.get('telefono', '')
        direccion = request.POST.get('direccion', '')

        Cliente.objects.create(
            nombre=nombre,
            email=email,
            telefono=telefono,
            direccion=direccion
        )

        return redirect('listar_clientes')
    return render(request, 'clientes/crear.html')

# Vista para editar clientes
def editar_clientes(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        cliente.nombre = request.POST['nombre']
        cliente.email = request.POST['email']
        cliente.telefono = request.POST.get('telefono', '')
        cliente.direccion = request.POST.get('direccion', '')
        cliente.save()

        return redirect('listar_clientes')
    
    return render(request, 'clientes/editar.html', {
        'cliente': cliente
    })

#Vista para elimianr clientes
def eliminar_clientes(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        cliente.delete()
        return redirect('listar_clientes')

    return render(request, 'clientes/eliminar.html',{
        'cliente': cliente
    })
