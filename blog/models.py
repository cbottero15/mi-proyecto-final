from pyexpat import model
# from typing_extensions import Required
from unittest.util import _MAX_LENGTH
from django.db import models
from traitlets import default

class Configuracion(models.Model):
    nombre_blog = models.CharField(max_length=14)
    construido_por = models.CharField(max_length=30)
    titulo_principal = models.CharField(max_length=30, default='')
    subtitulo_principal = models.CharField(max_length=60, default='')

    def __str__(self):
        return f"id:{self.id}, nombre:{self.nombre_blog}"
    
class Post(models.Model):
    title=models.CharField(max_length=100)
    short_content=models.CharField(max_length=255)
    contenido=models.TextField(max_length=3000)
    date_published=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"id:{self.id}, title:{self.title}"

class Category(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=100)

    def __str__(self):
        return f"id:{self.id}, nombre:{self.nombre}"
    
    
    
    
  
    

   