from django.shortcuts import render,redirect, get_object_or_404
from .models import Seccion

# Creacion de las vistas
# para listar secciones
def listar_secciones(request):
    secciones= Seccion.objects.all()
    return render(request, 'secciones/listar.html', {'secciones' : secciones})
# para crear secciones
def crear_secciones(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        Seccion.objects.create(nombre=nombre)
    
    return render(request, 'secciones/crear.html')
# para editar secciones
def editar_secciones(request, id):
     seccion = get_object_or_404(Seccion, id=id)
     if request.method == 'POST':
        seccion.nombre = request.POST['nombre']
        seccion.save()
        return redirect('listar_secciones')
    
     return render(request, 'secciones/editar.html', {'seccion': seccion})
# para elimintar secciones
def eliminar_secciones(request, id):
     seccion = get_object_or_404(Seccion, id=id)
     if request.method == 'POST':
        seccion.delete()
        return redirect('listar_secciones')
    
     return render(request, 'secciones/eliminar.html', {'seccion': seccion})

