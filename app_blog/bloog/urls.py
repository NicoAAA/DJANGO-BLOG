'''
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: DJANGO BLOG (bloog/urls.py)
FECHA: 2024-08-01
VERSION: 4.5.6
'''

# Importaciones desde django.
from django.urls import path
# Importaciones Locales
from .views import BlogListView


"""
Este módulo define las rutas URL para la aplicación de blog.
Importa el módulo `path` de `django.urls` y la vista `BlogListView` del módulo `views`.
Rutas definidas:
- La ruta raíz ('') que utiliza la vista `BlogListView` y se nombra 'home'.
"""


urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
]
