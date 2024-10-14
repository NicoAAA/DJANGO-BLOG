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
from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    """
    Modelo que representa una publicación en el blog.
    Atributos:
        title (CharField): Título de la publicación, con un máximo de 200 caracteres.
        author (ForeignKey): Autor de la publicación, relacionado con el modelo de usuario de Django.
        imagen (ImageField): Imagen opcional asociada a la publicación, almacenada en 'posts_images/'.
        body (TextField): Cuerpo del texto de la publicación.
    Métodos:
        __str__(): Retorna el título de la publicación.
        get_absolute_url(): Retorna la URL absoluta para la vista de detalle de la publicación.
    """
   
    title = models.CharField(max_length=200)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to='posts_images/', blank=True, null=True)
    body= models.TextField()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
