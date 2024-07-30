from django.db import models

class Stock(models.Model):
    cantidad_masas = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)