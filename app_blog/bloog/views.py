'''
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: DJANGO BLOG (bloog/models.py)
FECHA: 2024-08-01
VERSION: 4.5.6
'''

# Importaciones desde django.
from django.shortcuts import render
from django.views.generic import ListView

# Importacoiones locales
from .models import Post

# Create your views here.
class BlogListView(ListView):
    """
    Vista basada en clase que muestra una lista de publicaciones del blog.

    Atributos:
        model (Model): El modelo que se utilizará para obtener los datos. En este caso, es el modelo `Post`.
        template_name (str): El nombre de la plantilla que se utilizará para renderizar la vista. En este caso, es 'home.html'.
    """
    model = Post
    template_name = 'home.html'