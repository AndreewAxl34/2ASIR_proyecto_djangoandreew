from django.shortcuts import render,redirect, get_object_or_404
from .models import Administracion

# Crear las vistas de la administracion

#vista sobre lsitar administracion
def listar_administraciones(request):
    administraciones = Administracion.objects.all()
    return render(request, 'administraciones/listar.html', {
        'administraciones': administraciones
    })

#Vista para crear clientes
def crear_administraciones(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        sector_industrial = request.POST.get('sector_industrial')
        domicilio = request.POST.get('domicilio', '')
        telefono = request.POST.get('telefono', '')
        numero_empleados = request.POST.get('numero_empleados', 0)
        estructura_organizativa = request.POST.get('estructura_organizativa', '')
        tipo_iva = request.POST.get('tipo_iva', '')
        socios = request.POST.get('socios', '')

        Administracion.objects.create(
            nombre=nombre,
            sector_industrial=sector_industrial,
            domicilio=domicilio,
            telefono=telefono,
            numero_empleados=numero_empleados,
            estructura_organizativa=estructura_organizativa,
            tipo_iva=tipo_iva,
            socios=socios
        )

        return redirect('listar_administraciones')

    return render(request, 'administraciones/crear.html')

# vista para editar la administracion
def editar_administraciones(request, id):
    administracion = get_object_or_404(Administracion, id=id)

    if request.method == 'POST':
        administracion.nombre = request.POST.get('nombre')
        administracion.sector_industrial = request.POST.get('sector_industrial')
        administracion.domicilio = request.POST.get('domicilio', '')
        administracion.telefono = request.POST.get('telefono', '')
        administracion.numero_empleados = request.POST.get('numero_empleados', 0)
        administracion.estructura_organizativa = request.POST.get('estructura_organizativa', '')
        administracion.tipo_iva = request.POST.get('tipo_iva', '')
        administracion.socios = request.POST.get('socios', '')
        administracion.save()

        return redirect('listar_administraciones')

    return render(request, 'administraciones/editar.html', {
        'administracion': administracion
    })
# ista para  eliminiar la administracion
def eliminar_administraciones(request, id):
    administracion = get_object_or_404(Administracion, id=id)

    if request.method == 'POST':
        administracion.delete()
        return redirect('listar_administraciones')

    return render(request, 'administraciones/eliminar.html', {
        'administracion': administracion
    })



