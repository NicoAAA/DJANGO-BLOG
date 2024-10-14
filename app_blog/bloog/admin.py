'''
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: DJANGO BLOG (bloog/admin.py)
FECHA: 2024-08-01
VERSION: 4.5.6
'''

# Importaciones desde Django.
from django.contrib import admin
# Importaciones desde modulos locales.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    """
    Clase para personalizar la interfaz de administración del modelo Post.

    Atributos:
        list_display (tuple): Campos a mostrar en la lista de posts.
        fields (tuple): Campos a mostrar en el formulario de edición.
    """
    list_display = ('title', 'author', 'image')  # Campos a mostrar en la lista de posts
    fields = ('title', 'body', 'author', 'image')  # Campos a mostrar en el formulario de edición
   


# Register your models here.
admin.site.register(Post)
