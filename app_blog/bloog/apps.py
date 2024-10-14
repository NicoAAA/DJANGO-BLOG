'''
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: DJANGO BLOG (bloog/apps.py)
FECHA: 2024-08-01
VERSION: 4.5.6
'''



# Importaciones desde django.
from django.apps import AppConfig


class BloogConfig(AppConfig):
    """
    Configuración de la aplicación 'bloog'.
    Esta clase define la configuración predeterminada para la aplicación 'bloog'.
    Hereda de AppConfig y establece el campo automático predeterminado y el nombre
    de la aplicación.
    
    Atributos:
        default_auto_field (str): Especifica el tipo de campo automático predeterminado.
        name (str): Nombre de la aplicación.
    """
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bloog'
