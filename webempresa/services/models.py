from django.db import models

# Create your models here.
class Service(models.Model):
    titulo=models.CharField(max_length=200, verbose_name='Titulo')
    subtitulo=models.CharField(max_length=200, verbose_name='SubTitulo')
    contenido=models.TextField(verbose_name='Contenido')
    imagen=models.ImageField(verbose_name='Imagen', upload_to='services')
    creado=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')
    modificado=models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    class Meta:
        verbose_name='servicio'
        verbose_name_plural="servicios"
        ordering=['-creado'] 

    def __str__(self):
        return self.titulo
