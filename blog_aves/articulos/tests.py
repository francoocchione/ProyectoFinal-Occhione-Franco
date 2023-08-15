from django.test import TestCase      
from django.contrib.auth.models import User  
from articulos.models import Articulos


class ArticuloTests(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="testuser") 

    def test_creacion_articulo(self):
        articulo = Articulos(
            titulo="Titulo",
            subtitulo="Subtitulo",
            contenido="Contenido",
            autor=self.user,  # Set the autor field
        )
        articulo.save()

        self.assertEqual(Articulos.objects.count(), 1)
        self.assertEqual(articulo.titulo, "Titulo")
        self.assertEqual(articulo.subtitulo, "Subtitulo")
        self.assertEqual(articulo.contenido, "Contenido")

    def test_articulo_str(self):
        articulo = Articulos(
            titulo="Titulo",
            subtitulo="Subtitulo",
            contenido="Contenido",
            autor=self.user, 
        )
        articulo.save()

        self.assertEqual(articulo.__str__(), "Titulo, Subtitulo, Contenido")

