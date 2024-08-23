from App import views
from django.urls import path


urlpatterns = [
    path('inicio/', views.inicio, name="inicio"),
    path('base/', views.base, name="base"),
    path('conductores/', views.conductores, name="conductores"),
    path('guardas/', views.guardas, name="guardas"),
    path('operadores/', views.operadores, name="operadores"),
    path('base-formulario/', views.base_formulario, name="baseformulario"),
    path('base-formulario2/', views.base_formulario2, name="baseformulario2"),
    path('busqueda-base/', views.busquedabase, name="busqueda-base"),
    path('buscar/', views.buscar, name="buscar"),
    path('guarda-form/', views.guarda_formulario, name="guardaformulario"),
    path('conductor-form/', views.conductor_formulario, name="conductorformulario"),
    path('operador-form/', views.operador_formulario, name="operadorformulario"),
    path('busquedanombreconductor/', views.busqueda_nombreconductor, name="busquedanombreconductor"),
    path('buscarconductor/', views.buscarconductor, name="buscarconductor"),
    path('busquedanombreguarda/', views.busqueda_nombreguarda, name="busquedanombreguarda"),
    path('buscarguarda/', views.buscarguarda, name="buscarguarda"),
    path('busquedanombrebase/', views.busqueda_nombrebase, name="busquedanombrebase"),
    path('buscarbase/', views.buscarbase, name="buscarbase"),
    path('formularios/', views.vistaformularios, name="formularios"),
    path('formulariosdebusqueda/', views.vistaformulariosdebusqueda, name="formulariosbusqueda"),
]