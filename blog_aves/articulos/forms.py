from django import forms
from articulos.models import Aves, Articulos
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
import datetime

class ArticuloFormulario(forms.Form):
    titulo = forms.CharField(max_length=150)
    subtitulo = forms.CharField(max_length=150)
    #contenido = forms.CharField(widget=forms.Textarea(attrs={'class': 'ckeditor'}))
    contenido = forms.CharField(widget=CKEditorWidget())
    #autor = forms.CharField(max_length=150) 
    #fecha = forms.DateTimeField()
    foto = forms.FileField(required=False)
    



class AveFormulario(forms.Form):
    orden = forms.CharField(required=True, max_length=200)
    familia = forms.CharField(required=True, max_length=200)
    especie = forms.CharField(required=True, max_length=200)
    nombre = forms.CharField(required=True, max_length=200)
    caracteristicas = forms.CharField(widget=forms.Textarea)
    ultima_observacion = forms.DateField()
    foto = forms.FileField(required=False)
    audio = forms.FileField(required=False)