from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    disponible = models.BooleanField()
    masasxunidad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}"