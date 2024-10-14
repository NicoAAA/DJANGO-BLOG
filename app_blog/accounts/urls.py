'''
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: DJANGO BLOG (accounts/url.py)
FECHA: 2024-08-01
VERSION: 4.5.6
'''

""" 
Importa:
- path: Función de Django para definir rutas URL.
- SignUpView: Vista basada en clase para el registro de usuarios.
- LogoutView: Vista basada en clase para el cierre de sesión de usuarios.
"""
from .views import SignUpView, LogoutView
from django.urls import path 

"""
Este módulo define las rutas URL para la aplicación de cuentas.
Rutas:
- 'signup/': Muestra la vista de registro de usuario (SignUpView).
- 'logout/': Muestra la vista de cierre de sesión (LogoutView).
"""

urlpatterns = [
    path ('signup/', SignUpView.as_view(), name= 'signup'),
    path('logout/',LogoutView.as_view(), name= 'logout'),
]
