## Buenas, les brindo instrucciones para manejar la pagina web sobre las Aves de Argentina:

- En la pagina inicio hay una breve introduccion sobre la pagina y sus funcionalidades.
- Las secciones son: Las Aves, Publicaciones, Acerca de mi y los botones de Iniciar Sesion y Registrarse
- Las Aves: En esta seccion se pueden observar algunas de las aves de interes (por cuestiones de tiempo no pude
cargar todas) y visualizar nombre, especie, orden, familia, caracteristicas, una foto y un audio para escuchar su canto
- Publicaciones: Cualquier visitante de la pagina puede ver las publicaciones que suben los usuarios, si te registras podes ademas subir publicaciones editar/eliminar las tuyas.
- Acerca de mi: Habla acerca del creador de la pagina.
- Para registrarte debes clickear el boton 'Registrate', te solicitara tus datos.
- Para iniciar sesion debes clickear el boton 'Iniciar sesion' donde debes colocar tu nombre de usuario y contra
senia previamente registrado.
- Es posible buscar tanto un ave como una publicacion a traves de un buscador. Las aves se buscan por nombre y
las publicaciones por titulo


# Instrucciones para entrar al panel aministrativo de Django

## En consola, crear un superuser:
python manage.py createsuperuser

## Acceder con user y password via:
```
127.0.0.1:8000/admin
```

## Superusuario:
username:admin
contraseña:superuser2019

## Usuarios normales:
username: franocchione96
contraseña: River91218

## Para hacer prueba Unit Test automatizado:
En terminal: cd blog_aves python manage.py test (visualizar archivo tests.py dentro de app 'articulos')