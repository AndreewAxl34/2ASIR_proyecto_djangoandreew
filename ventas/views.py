from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.shortcuts import render, redirect
import json

class Persona(object):

    def __init__(self, nombre, apellido):
        
        self.nombre=nombre

        self.apellido=apellido

def saludo(request): # Primera vista de ejemplo

    p1=Persona(" Profesor Juan", "Diaz")

    #nombre="Juan"

    #apellido="diaz"

    ahora=datetime.datetime.now()

    doc_externo=open("/home/usuario/proyecto_django/ventas/ventas/plantillas/plantillaeejmplo.html")

    plt=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "fecha_ahora":ahora})

    documento =plt.render(ctx)

    return HttpResponse(documento)

def despedida(request): # Primera vista de ejemplo
    return HttpResponse("Hasta lueg DJANGo")

def dameFecha(request):

    fecha_actual=datetime.datetime.now()

    documento="""<html>
      <body>
        <h1>
        Fecha y hora actales %s
        </h1>
      </body>
    </html>""" %fecha_actual

    return HttpResponse(documento)

def calculaEdad(request,edad,agno): # Primera vista de ejemplo
    #edadActual=18
    periodo=agno-2019
    edadFutura=edad+periodo
    documento="""<html>
      <body>
        <h1>
        En el año %s tendras %s años
        </h1>
      </body>
    </html>""" %(agno, edadFutura)

    return HttpResponse(documento)
# funcion para mostrar la plantilla de inicio.html
def inicio(request):
    return render(request, 'inicio.html')

#configuracion vistas
# funcion para leer y guardar el ficherp

def leer_configuracion():
    with open("configuracion.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
    return datos

def guardar_configuracion(datos):
    with open("configuracion.json", "w", encoding="utf-8") as archivo:
      json.dump(datos, archivo, indent=4, ensure_ascii=False)

def configuracion(request):
    datos=leer_configuracion()

    if request.method == "POST":
        datos["nombre"] = request.POST.get("nombre")
        datos["sector_industrial"] = request.POST.get("sector_industrial")
        datos["domicilio"] = request.POST.get("domicilio")
        datos["telefono"] = request.POST.get("telefono")
        datos["numero_empleados"] = request.POST.get("numero_empleados")
        datos["estructura_organizativa"] = request.POST.get("estructura_organizativa")
        datos["tipo_iva"] = request.POST.get("tipo_iva")
        datos["socios"] = request.POST.get("socios")

        guardar_configuracion(datos)
        return redirect("configuracion")
    
    return render(request, "configuracion.html", {"config": datos})


