from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.shortcuts import render

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

