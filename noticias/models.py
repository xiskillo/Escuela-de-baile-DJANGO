from django.db import models
from ckeditor.fields import RichTextField

class Noticia(models.Model):
    titulo = models.CharField(verbose_name="Título", max_length=200)
    contenido = RichTextField(verbose_name="Contenido")
    orden = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "noticia"
        verbose_name_plural = "noticias"
        ordering = ['orden', 'titulo']
        

    def __str__(self):
        return self.titulo