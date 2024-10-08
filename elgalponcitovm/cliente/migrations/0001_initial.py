# Generated by Django 5.0.7 on 2024-07-19 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('telefono', models.CharField(max_length=20)),
                ('cantidad', models.IntegerField()),
                ('detalles', models.TextField()),
                ('monto', models.IntegerField()),
                ('estado', models.CharField(choices=[('tomado', 'Tomado'), ('en_proceso', 'En Proceso'), ('terminado', 'Terminado'), ('entregado', 'Entregado')], default='tomado', max_length=15)),
                ('horario', models.CharField(choices=[('sin_especificar', 'Cuando este lista'), ('20:00', '20:00'), ('20:20', '20:20'), ('20:40', '20:40'), ('21:00', '21:00'), ('21:20', '21:20'), ('21:40', '21:40'), ('22:00', '22:00'), ('22:20', '22:20'), ('22:40', '22:40'), ('23:00', '23:00'), ('23:20', '23:20'), ('23:40', '23:40'), ('00:00', '00:00')], default='sin_especificar', max_length=20)),
                ('medio_pago', models.CharField(choices=[('efectivo', 'Efectivo'), ('transferencia', 'Transferencia/MP')], default='efectivo', max_length=15)),
                ('metodo_entrega', models.CharField(choices=[('retiro', 'Retiro por local'), ('envio', 'Envio a domicilio')], default='envio', max_length=15)),
                ('direccion', models.CharField(blank=True, max_length=200, null=True)),
                ('observaciones', models.TextField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]
