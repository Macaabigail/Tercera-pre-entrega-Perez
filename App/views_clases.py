from django.shortcuts import render  # Para renderizar plantillas HTML
from .models import Conductor , Base , Guarda # Importa el modelo "Curso" desde tu aplicación
from django.views.generic import ListView  # Para mostrar listas de objetos
from django.views.generic.detail import DetailView  # Para mostrar detalles de un objeto
from django.views.generic.edit import CreateView, UpdateView, DeleteView  # Para crear, actualizar y eliminar objetos
from django.urls import reverse_lazy  # Para generar URLs de forma segura

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm  # Formularios de autenticación de usuarios
from django.contrib.auth import login, logout, authenticate  # Funciones para gestionar inicios de sesión y autenticación
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required




class ConductorListView(LoginRequiredMixin, ListView):
   
    model = Conductor  # Modelo con el que trabaja esta vista
    context_object_name = "conductores"
    template_name = "App/conductor_list.html" # Plantilla para renderizar la lista

class ConductorDetalle(LoginRequiredMixin, DetailView):

    model = Conductor
    template_name = "App/conductor_detalle.html"
    
class ConductorCreateView(LoginRequiredMixin, CreateView):

    model = Conductor
    template_name = "App/conductor_crear.html"
    success_url = reverse_lazy("List")  # URL de redirección después de crear un curso
    fields = ["nombre", "apellido","categoria"]  # Campos del modelo a mostrar en el formulario

class ConductorUpdateView(LoginRequiredMixin, UpdateView):

    model = Conductor
    template_name = "App/conductor_edit.html"
    # success_url = reverse_lazy("List")
    success_url = reverse_lazy("List")  # Otra forma de especificar la URL de redirección
    fields = ["nombre", "apellido","categoria"]

class ConductorDeleteView(LoginRequiredMixin, DeleteView):
    """
    Vista para eliminar cursos.
    """
    model = Conductor
    success_url = reverse_lazy("List")  # URL de redirección después de eliminar un curso
    template_name = "App/conductor_confirm_delete.html"  # Plantilla para confirmar la eliminación


class BaseListView(ListView):
   
    model = Base  # Modelo con el que trabaja esta vista
    context_object_name = "base"
    template_name = "App/base_list.html" # Plantilla para renderizar la lista

class BaseDetalle(DetailView):

    model = Base
    template_name = "App/base_detalle.html"
    
class BaseCreateView(CreateView):

    model = Base
    template_name = "App/base_crear.html"
    success_url = reverse_lazy("Listbase")  
    fields = ["nombre"]  

class BaseUpdateView(UpdateView):

    model = Base
    template_name = "App/base_edit.html"
 
    success_url = reverse_lazy("Listbase")  
    fields = ["nombre"]

class BaseDeleteView(DeleteView):
    model = Base
    success_url = reverse_lazy("Listbase")  
    template_name = "App/base_confirm_delete.html"  

class GuardaListView(ListView):
   
    model = Guarda 
    context_object_name = "guardas"
    template_name = "App/guarda_list.html"

class GuardaDetalle(DetailView):

    model = Guarda
    template_name = "App/guarda_detalle.html"
    
class GuardaCreateView(CreateView):

    model = Guarda
    template_name = "App/guarda_crear.html"
    success_url = reverse_lazy("Listguarda")  # URL de redirección después de crear un curso
    fields = ["nombre", "apellido","categoria"]  # Campos del modelo a mostrar en el formulario

class GuardaUpdateView(UpdateView):

    model = Guarda
    template_name = "App/guarda_edit.html"
    success_url = reverse_lazy("Listguarda")  
    fields = ["nombre", "apellido","categoria"]

class GuardaDeleteView(DeleteView):

    model = Guarda
    success_url = reverse_lazy("Listguarda") 
    template_name = "App/guarda_confirm_delete.html" 
