'''
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: DJANGO BLOG (settings.py)
FECHA: 2024-08-01
VERSION: 4.5.6
'''

# Importaciones desde django.
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.

class SignUpView(CreateView):
    """
    Clase con la que se crea la vista del login

    Args:
        CreateView (class): Clase con la que se crea la vista del login
        usando clases de django.
    
    """
    form_class= UserCreationForm
    success_url= reverse_lazy('login')
    template_name = 'registration/signup.html'


class LogoutView(CreateView):
    """
    Clase con la que se crea la vista del login

    Args:
        CreateView (class): Clase con la que se crea la vista del login
        usando clases de django.
    
    """
    
    form_class= UserCreationForm
    success_url= reverse_lazy('login')
    template_name= 'registration/logout.html' 
    
    