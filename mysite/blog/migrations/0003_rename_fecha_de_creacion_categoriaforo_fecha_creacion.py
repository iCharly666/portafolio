# Generated by Django 4.1.7 on 2023-07-17 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_fecha_creacion_categoriaforo_fecha_de_creacion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoriaforo',
            old_name='fecha_de_creacion',
            new_name='fecha_creacion',
        ),
    ]