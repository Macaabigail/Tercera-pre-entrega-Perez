from django.shortcuts import render
from django.http import HttpResponse
from App.models import Guarda, Base, Conductor, Operador
from App.forms import Baseformulario, Guardaformulario, Conductoresformulario, Operadoresformulario, Buscar

from django.contrib.auth.decorators import login_required


def inicio(request):
    return render (request, 'app/padre.html')
@login_required
def base(request):
    return render(request, 'app/base.html')
@login_required
def conductores(request):
    return render(request, 'app/conductores.html')
@login_required
def guardas(request):
    return render(request, 'app/guardas.html')
@login_required
def operadores(request):
    return render(request, 'app/operadores.html')

def base_formulario(request):
    if request.method == 'POST':
        base = Base(nombre=request.POST['base'])
        base.save()
        return render(request, "App/padre.html")
    return render(request, "App/baseformulario.html")
@login_required

def base_formulario2(request):
    if request.method == "POST":
        miFormulario = Baseformulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            base = Base(nombre=informacion["base"])
            base.save()
            return render(request, "App/padre.html")
    else:
        miFormulario = Baseformulario()
    return render(request, "App/baseformulario2.html", {"miFormulario": miFormulario})
@login_required
def busquedabase(request):
    return render(request, "App/busquedabase.html")
@login_required
def buscar(request):
    respuesta = f"estoy buscando la base: {request.GET.get('base', '') }"
    return HttpResponse(respuesta)
@login_required
def guarda_formulario(request):
    if request.method == "POST":
        miFormulario = Guardaformulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            guarda = Guarda(nombre=informacion["nombre"], apellido=informacion["apellido"], categoria=informacion["categoria"])
            guarda.save()
            return render(request, "App/padre.html")
    else:
        miFormulario = Guardaformulario()
    return render(request, "App/guardasformulario.html", {"miFormulario": miFormulario})
@login_required
def conductor_formulario(request):
    if request.method == "POST":
        miFormulario = Conductoresformulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            conductor = Conductor(nombre=informacion["nombre"], apellido=informacion["apellido"], categoria=informacion["categoria"])
            conductor.save()
            return render(request, "App/padre.html")
    else:
        miFormulario = Conductoresformulario()
    return render(request, "App/conductorformulario.html", {"miFormulario": miFormulario})
@login_required
def operador_formulario(request):
    if request.method == "POST":
        miFormulario = Operadoresformulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            operador = Operador(nombre=informacion["nombre"], apellido=informacion["apellido"], categoria=informacion["categoria"])
            operador.save()
            return render(request, "App/padre.html")
    else:
        miFormulario = Operadoresformulario()
    return render(request, "App/operadorformulario.html", {"miFormulario": miFormulario})

def busqueda_nombreconductor(request):
    return render(request, "App/busquedanombreconductor.html")
@login_required
def buscarconductor(request):
    nombre = request.GET.get('nombre', '').strip()
    if nombre:
        conductores = Conductor.objects.filter(nombre__icontains=nombre)
        return render(request, "App/resultadobusquedanombreconductor.html", {"conductores": conductores, "nombre": nombre})
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)
@login_required
def busqueda_nombreguarda(request):
    return render(request, "App/busquedanombreguarda.html")
@login_required
def buscarguarda(request):
    nombre = request.GET.get('nombre', '').strip()
    if nombre:
        guardas = Guarda.objects.filter(nombre__icontains=nombre)
        return render(request, "App/resultadobusquedanombreguarda.html", {"guardas": guardas, "nombre": nombre})
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)
@login_required
def busqueda_nombrebase(request):
    return render(request, "App/busquedanombrebase.html")
@login_required
def buscarbase(request):
    nombre = request.GET.get('nombre', '').strip()
    if nombre:
        base = Base.objects.filter(nombre__icontains=nombre)
        return render(request, "App/resultadobusquedanombrebase.html", {"base": base, "nombre": nombre})
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)
@login_required
def vistaformularios(request):
    return render(request, 'app/formularios.html')
@login_required
def vistaformulariosdebusqueda(request):
    return render(request, 'app/formulariodebusqueda.html')
@login_required
def leerconductor(request):
    conductores = Conductor.objects.all()
    contexto = {"conductores": conductores}
    return render(request, "App/leerconductores.html", contexto)
@login_required
def eliminarconductor(request, conductores_nombre):
    conductores = Conductor.objects.get(nombre=conductores_nombre)
    conductores.delete()
    conductores = Conductor.objects.all()
    contexto = {"conductores": conductores}
    return render(request, "App/leerconductores.html", contexto)


def acerca_de_mi(request):
    return render(request, "App/acercademi.html")