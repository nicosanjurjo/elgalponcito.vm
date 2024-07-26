from django.db import models
from zonas.models import Zona

class Turno(models.Model):
    horario = models.TimeField()
    max_pedidos = models.IntegerField(default=10)
    pedidos_actuales = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.horario}"

    def disponible(self):
        return self.pedidos_actuales < self.max_pedidos

class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('tomado', 'Tomado'),
        ('en_proceso', 'En Proceso'),
        ('terminado', 'Terminado'),
        ('entregado', 'Entregado')
    ]

    PAGO_CHOICES = [
        ('efectivo', 'Efectivo'),
        ('transferencia', 'Transferencia/MP')
    ]

    ENTREGA_CHOICES = [
        ('retiro', 'Retiro por local'),
        ('envio', 'Envio a domicilio')
    ]

    nombre = models.CharField(max_length=25)
    telefono = models.CharField(max_length=20)
    cantidad = models.IntegerField()
    detalles = models.TextField()  # Este campo almacenará los detalles del pedido en formato JSON o texto plano.
    monto = models.IntegerField()
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES, default='tomado')
    horario = models.CharField(max_length=5, null=True, blank=True)
    medio_pago = models.CharField(max_length=15, choices=PAGO_CHOICES, default='efectivo')
    metodo_entrega = models.CharField(max_length=15, choices=ENTREGA_CHOICES, default='retiro')
    direccion = models.CharField(max_length=200, blank=True, null=True)
    observaciones = models.TextField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f"Pedido #{self.id} - {self.nombre}"
