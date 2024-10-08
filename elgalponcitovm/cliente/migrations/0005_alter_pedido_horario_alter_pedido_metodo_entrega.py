# Generated by Django 5.0.7 on 2024-07-23 23:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_rename_hora_turno_horario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='horario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.turno'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='metodo_entrega',
            field=models.CharField(choices=[('retiro', 'Retiro por local'), ('envio', 'Envio a domicilio')], default='retiro', max_length=15),
        ),
    ]
