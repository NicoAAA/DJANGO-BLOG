'''
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: DJANGO BLOG (accounts/apps.py)
FECHA: 2024-08-01
VERSION: 4.5.6
'''



# importaciones desde Django.
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """
    Configuración de la aplicación 'accounts'.

    Esta clase define la configuración predeterminada para la aplicación 'accounts'.
    Hereda de AppConfig y establece el campo automático predeterminado y el nombre de la aplicación.

    Atributos:
        default_auto_field (str): Especifica el tipo de campo automático predeterminado para los modelos en esta aplicación.
        name (str): Nombre de la aplicación.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
