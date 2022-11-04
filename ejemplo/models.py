from django.db import models

class Familiar(models.Model):
      apellido = models.CharField(max_length=30)
      nombre = models.CharField(max_length=40)
      direccion = models.CharField(max_length=60)
      localidad = models.CharField(max_length=40)
      numero_pasaporte = models.IntegerField()
     # creado_el = models.DateField(auto_created=True)

def __str__(self):
      return f"{self.apellido}, {self.nombre}, {self.localidad}, {self.id}"
