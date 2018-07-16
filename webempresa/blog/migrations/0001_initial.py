# Generated by Django 2.0.2 on 2018-07-15 17:59

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categoria',
                'ordering': ['-creado'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titulo')),
                ('conten', models.TextField(verbose_name='Contenido')),
                ('published', models.DateTimeField(default=datetime.datetime(2018, 7, 15, 17, 59, 35, 222163, tzinfo=utc), verbose_name='Fecha de publicación')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog', verbose_name='Imagen')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
                ('categories', models.ManyToManyField(to='blog.Category', verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'entrada',
                'verbose_name_plural': 'entradas',
                'ordering': ['-creado'],
            },
        ),
    ]
