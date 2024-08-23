from django.shortcuts import render
from django.http import HttpResponse
from App.models import Guarda,Base,Conductor,Operador
from App.forms import Baseformulario, Guardaformulario, Conductoresformulario, Operadoresformulario, Buscar

def inicio(request):
    return render(request, 'app/padre.html')


def base(request):
    return render(request, 'app/base.html')

def conductores(request):
    return render(request, 'app/conductores.html')

def guardas(request):
    return render(request, 'app/guardas.html')

def operadores(req):
    return render(req, 'app/operadores.html')

def base_formulario(request):
    if request.method == 'POST':
        base = Base(nombre=request.POST['base'])
        base.save()
        
        return render(request,"App/padre.html")
    
    return render(request,"App/baseformulario.html")
        
def base_formulario2(request):
    if request.method == "POST":
        miFormulario = Baseformulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            base = Base(nombre=informacion["base"])
            base.save()
            return render(request, "App/padre.html")  # Redirigimos a la página de inicio
    else:
        miFormulario = Baseformulario()  # Creamos un formulario vacío para mostrarlo inicialmente

    return render(request, "App/baseformulario2.html", {"miFormulario": miFormulario})

def busquedabase(request):
     return render(request, "App/busquedabase.html")
 
def buscar(request):
    
    respuesta = f"estoy buscando la base: {request.GET['base'] }"
    
    return HttpResponse(respuesta)


def guarda_formulario(request):


      if request.method == "POST":

 

            miFormulario = Guardaformulario(request.POST) # Aqui me llega la informacion del html

            print(miFormulario)

 

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  guarda = Guarda(nombre=informacion["nombre"], apellido=informacion["apellido"], categoria=informacion["categoria"])

                  guarda.save()

                  return render(request, "App/padre.html")

      else:

            miFormulario = Guardaformulario()

 

      return render(request, "App/guardasformulario.html", {"miFormulario": miFormulario})


def conductor_formulario(request):


      if request.method == "POST":

 

            miFormulario = Conductoresformulario(request.POST) # Aqui me llega la informacion del html

            print(miFormulario)

 

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  conductor = Conductor(nombre=informacion["nombre"], apellido=informacion["apellido"], categoria=informacion["categoria"])

                  conductor.save()

                  return render(request, "App/padre.html")

      else:

            miFormulario = Conductoresformulario()

 

      return render(request, "App/conductorformulario.html", {"miFormulario": miFormulario})
  
def operador_formulario(request):


      if request.method == "POST":

 

            miFormulario = Operadoresformulario(request.POST) # Aqui me llega la informacion del html

            print(miFormulario)

 

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  operador = Operador(nombre=informacion["nombre"], apellido=informacion["apellido"], categoria=informacion["categoria"])

                  operador.save()

                  return render(request, "App/padre.html")

      else:

            miFormulario = Operadoresformulario()

 

      return render(request, "App/operadorformulario.html", {"miFormulario": miFormulario})
  
  
def busqueda_nombreconductor(request):
       return render(request, "App/busquedanombreconductor.html")



def buscarconductor(request):
    nombre = request.GET.get('nombre', '').strip()
    
    if nombre:
        conductores = Conductor.objects.filter(nombre__icontains=nombre)
        return render(request, "App/resultadobusquedanombreconductor.html", {"conductores": conductores, "nombre": nombre})
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)
    
    
def busqueda_nombreguarda(request):
       return render(request, "App/busquedanombreguarda.html")



def buscarguarda(request):
    nombre = request.GET.get('nombre', '').strip()
    
    if nombre:
        guardas = Guarda.objects.filter(nombre__icontains=nombre)
        return render(request, "App/resultadobusquedanombreguarda.html", {"guardas": guardas, "nombre": nombre})
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)
    
    
def busqueda_nombrebase(request):
       return render(request, "App/busquedanombrebase.html")



def buscarbase(request):
    nombre = request.GET.get('nombre', '').strip()
    
    if nombre:
        base = Base.objects.filter(nombre__icontains=nombre)
        return render(request, "App/resultadobusquedanombrebase.html", {"base": base, "nombre": nombre})
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)
    
    
def vistaformularios(req):
    return render(req, 'app/formularios.html')

def vistaformulariosdebusqueda(req):
    return render(req, 'app/formulariodebusqueda.html')