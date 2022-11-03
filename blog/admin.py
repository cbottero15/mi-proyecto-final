from django.contrib import admin
from blog.models import Configuracion, Post, Categoria

admin.site.register(Configuracion)
admin.site.register(Post)
admin.site.register(Categoria)

# Register your models here.
