
from typing import Any, Optional
from django.db import models
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LogoutView
from perfiles.forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from perfiles.forms import AvatarFormulario
from perfiles.models import Avatar


def registro(request):
   if request.method == "POST":
       formulario = UserRegisterForm(request.POST)

       if formulario.is_valid():
           formulario.save()  # Esto lo puedo usar porque es un model form
           url_exitosa = reverse('inicio')
           return redirect(url_exitosa)
   else:  # GET
       formulario = UserRegisterForm()
   return render(
       request=request,
       template_name='perfiles/registro.html',
       context={'form': formulario},
   )

def login_view(request):
   next_url = request.GET.get('next') 
   if request.method == "POST":
       form = AuthenticationForm(request, data=request.POST)

       if form.is_valid():
           data = form.cleaned_data
           usuario = data.get('username')
           password = data.get('password')
           user = authenticate(username=usuario, password=password)
           # user puede ser un usuario o None
           if user:
               login(request=request, user=user)
               url_exitosa = reverse('inicio')
               return redirect(url_exitosa)
   else:  # GET
       form = AuthenticationForm()
   return render(
       request=request,
       template_name='perfiles/login.html',
       context={'form': form},
   )

#clase basada en vista para logout:   
class CustomLogoutView(LogoutView):
   template_name = 'perfiles/logout.html'

#Vista basada en clase que hereda de LoginRequiredMixin y UpdateView
class MiPerfilUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserUpdateForm
    success_url = reverse_lazy('inicio')
    template_name = 'perfiles/formulario_perfil.html'
    #para que retorne el usuario que esta haciendo la peticion
    def get_object(self, queryset=None):
        return self.request.user

def agregar_avatar(request):
    if request.method == "POST":
        formulario = AvatarFormulario(request.POST, request.FILES)
        
        if formulario.is_valid():
            avatar = formulario.save(commit=False)  # Don't save yet
            avatar.user = request.user  # Assign user to the avatar
            
            existing_avatar = Avatar.objects.filter(user=request.user).first()
        if existing_avatar:
                # If an existing avatar is found, update its fields
            existing_avatar.imagen = avatar.imagen  # Update avatar image field
            existing_avatar.save()  # Save the changes to the existing avatar
        else:
                # If no existing avatar, save the new avatar
            avatar.save()  # Save the new avatar
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:
        formulario = AvatarFormulario()
    return render(
        request=request,
        template_name="perfiles/formulario_avatar.html",
        context={'form': formulario},
    )
#def agregar_avatar(request):
#    if request.method == "POST":
#        formulario = AvatarFormulario(request.POST, request.FILES)
#        
#        if formulario.is_valid():
#            avatar = formulario.save()
#            avatar.user = request.user #asigno usuario al avatar
#            avatar.save()
#            url_exitosa = reverse('inicio')
#            return redirect(url_exitosa)
#    else:
#        formulario = AvatarFormulario()
#    return render(
#        request=request,
#        template_name="perfiles/formulario_avatar.html",
#        context={'form': formulario},
#    )
