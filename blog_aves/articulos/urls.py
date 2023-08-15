from django.contrib import admin
from django.urls import path
from articulos.views import *

urlpatterns = [
    path('aves/', mostrar_aves, name="lista_aves"),
    path('buscar-ave/', buscar_aves, name='buscar_aves'),
    path('aves/<int:pk>/', AvesDetailView.as_view(), name="ver_ave"),
    path('articulos/', mostrar_articulos, name="lista_articulos"),
    path('crear-articulo', crear_articulo, name="crear_articulo"),
    path('buscar-articulo', buscar_articulos, name="buscar_articulos"),
    path('articulos/<int:pk>/', ArticulosDetailView.as_view(), name="ver_articulos"),
    path('editar-articulo/<int:id>/', editar_articulo, name = "editar_articulo"),
    path('eliminar-articulo/<int:id>/', eliminar_articulo, name = "eliminar_articulo"),
]