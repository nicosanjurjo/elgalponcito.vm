# Generated by Django 5.0.7 on 2024-08-03 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0007_alter_producto_masasxunidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='masasxunidad',
            field=models.DecimalField(decimal_places=1, max_digits=1),
        ),
    ]
