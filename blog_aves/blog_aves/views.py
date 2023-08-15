from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def inicio(request): #pagina inicio
    contexto = {}
    http_response = render(
        request=request,
        template_name='inicio.html',
        context=contexto,
    )
    return http_response

def acerca_de(request): #pagina acerca de
    contexto = {}
    http_response = render(
        request=request,
        template_name='acerca_de.html',
        context=contexto,
    )
    return http_response