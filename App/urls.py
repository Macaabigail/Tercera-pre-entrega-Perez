from App import views
from django.urls import path
from App import views_clases



urlpatterns = [
    path('', views.inicio, name="inicio"),
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
    path('leerconductor/', views.leerconductor, name="leerconductor"),
    path('eliminarconductor/<str:conductor_nombre>/', views.eliminarconductor, name="eliminarconductor"),
    path('acercademi/', views.acerca_de_mi, name="acercademi")
]

urls_vistas_clases = [
    path('clases/listaconductores/', views_clases.ConductorListView.as_view(), name='List'),
    path('clases/detalleconductores/<int:pk>/', views_clases.ConductorDetalle.as_view(), name='Detail'),
    path('clases/nuevoconductores/', views_clases.ConductorCreateView.as_view(), name='New'),
    path('clases/editarconductores/<int:pk>/', views_clases.ConductorUpdateView.as_view(), name='Edit'),
    path('clases/eliminarconductores/<int:pk>/', views_clases.ConductorDeleteView.as_view(), name='Delete'),
    path('clases/listabase/', views_clases.BaseListView.as_view(), name='Listbase'),
    path('clases/detallebase/<int:pk>/', views_clases.BaseDetalle.as_view(), name='Detailbase'),
    path('clases/nuevabase/', views_clases.BaseCreateView.as_view(), name='New'),
    path('clases/editarbase/<int:pk>/', views_clases.BaseUpdateView.as_view(), name='Editbase'),
    path('clases/eliminarbase/<int:pk>/', views_clases.BaseDeleteView.as_view(), name='Deletebase'),
    path('clases/listaguarda/', views_clases.GuardaListView.as_view(), name='Listguarda'),
    path('clases/detalleguarda/<int:pk>/', views_clases.GuardaDetalle.as_view(), name='Detailguarda'),
    path('clases/nuevoguarda/', views_clases.GuardaCreateView.as_view(), name='New'),
    path('clases/editarguarda/<int:pk>/', views_clases.GuardaUpdateView.as_view(), name='Editguarda'),
    path('clases/eliminarguarda/<int:pk>/', views_clases.GuardaDeleteView.as_view(), name='Deleteguarda'),
    
    
]

urlpatterns += urls_vistas_clases
    
    
