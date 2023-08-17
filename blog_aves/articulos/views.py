
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from articulos.models import Aves, Articulos
from articulos.forms import *
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

#from django.contrib.auth.decorators import login_required

def mostrar_articulos(request):
    contexto = {
        "articulos" : Articulos.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='articulos/mostrar_articulos.html',
        context=contexto,
    )
    return http_response

def crear_articulo(request):
    if request.method == 'POST':
        formulario = ArticuloFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            data = formulario.cleaned_data
            titulo = data['titulo']
            subtitulo = data['subtitulo']
            contenido = data['contenido']
            foto = data['foto']
            #fecha = data['fecha']
            autor = request.user
            articulo = Articulos(titulo=titulo, subtitulo=subtitulo, contenido=contenido, foto=foto, autor=autor)
            articulo.save()
            url_exitosa = reverse('lista_articulos')
            return redirect(url_exitosa)
    else:
        formulario = ArticuloFormulario()
    http_response = render(
        request = request,
        template_name='articulos/formulario_articulos.html',
        context={'formulario' : formulario}
    )
    return http_response

def editar_articulo(request, id):
    articulo = Articulos.objects.get(id=id)
    if request.method == 'POST':
        formulario = ArticuloFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            data = formulario.cleaned_data
            articulo.titulo = data['titulo']
            articulo.subtitulo = data['subtitulo']
            articulo.contenido = data['contenido']
            #articulo.fecha = data['fecha']
            if data['foto']:
                articulo.foto = data['foto']
            articulo.save()
            url_exitosa = reverse('lista_articulos')
            return redirect(url_exitosa)
    else:
        inicial = { #le paso al form esta data inicial para que aparezcan los datos completados al ingresar a 'editar' y luego los puedo modificar
            'titulo' : articulo.titulo,
            'subtitulo' : articulo.subtitulo,
            'contenido' : articulo.contenido,
            #'fecha' : articulo.fecha, 
            'foto' : articulo.foto,
        }
        formulario = ArticuloFormulario(initial=inicial)
        return render(
            request=request,
            template_name='articulos/formulario_articulos.html',
            context={'formulario': formulario},
        )
        
def eliminar_articulo(request, id):
    articulo = Articulos.objects.get(id=id)
    if request.method == 'POST':
        articulo.delete()
        url_exitosa = reverse('lista_articulos')
        return redirect(url_exitosa)
    else:
        return render(
        request,
        'articulos/eliminar_articulo.html', 
        {'articulo': articulo}
    )

def mostrar_aves(request):
    contexto = {
        "aves" : Aves.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='articulos/mostrar_aves.html',
        context=contexto,
    )
    return http_response


def buscar_aves(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        aves = Aves.objects.filter(nombre__contains=busqueda)
        contexto = {
            "aves" : aves,
        }
        http_response = render(
            request = request,
            template_name='articulos/mostrar_aves.html',
            context = contexto,
        )
        return http_response
    
class AvesDetailView(DetailView):
   model = Aves
   success_url = reverse_lazy('lista_aves')
   
def buscar_articulos(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        articulos = Articulos.objects.filter(titulo__contains=busqueda)
        contexto = {
            "articulos" : articulos,
        }
        http_response = render(
            request = request,
            template_name='articulos/mostrar_articulos.html',
            context = contexto,
        )
        return http_response
    
class AvesDetailView(DetailView):
   model = Aves
   success_url = reverse_lazy('lista_aves')
   
class ArticulosDetailView(DetailView):
   model = Articulos
   success_url = reverse_lazy('lista_articulos')