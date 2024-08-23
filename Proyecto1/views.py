from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from App.models import Base

def saludo(request):
    return HttpResponse("Hola")

def otra_vista(request):
    return HttpResponse("<h1>¡Esto es un título!</h1><p>Y este es un párrafo.</p>")



def probando_template(request):
    
    nom = "Maca"
    ap = "Perez"
    diccionario_de_contexto = {'nombre': nom, 'apellido': ap}
    
   
   
    plantilla = loader.get_template('template1.html')
    documento = plantilla.render(diccionario_de_contexto)
    

    return HttpResponse(documento)


def agregar_base(request, nom):
    nombre = Base(nombre=nom)
    nombre.save()
    
    return HttpResponse("Base agregada")