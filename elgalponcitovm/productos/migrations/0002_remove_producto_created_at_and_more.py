# Generated by Django 5.0.7 on 2024-07-18 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='updated_at',
        ),
    ]
