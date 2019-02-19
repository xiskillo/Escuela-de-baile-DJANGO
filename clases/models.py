from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


# Create your models here.
class Profesores(models.Model):
    nombre=models.CharField(max_length=200, verbose_name="Nombre")
    email=models.EmailField(max_length=100, blank=True, null=True, verbose_name="EMAIL")
    telefono=models.IntegerField(blank=True, null=True, verbose_name="Teléfono")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")

    class Meta:
        verbose_name="Profesor"
        verbose_name_plural="Profesores"
        ordering=['-created']

    def __str__(self):
        return self.nombre

class Aulas(models.Model):
    nombre=models.CharField(max_length=30, verbose_name="Nombre del Aula")
    profesores=models.ManyToManyField(Profesores, verbose_name=("Profesores"), related_name="profesor")
    fecha=models.DateTimeField(verbose_name="Fecha de reserva", default=now)
    administrador=models.ForeignKey(User,verbose_name="Administrador",on_delete=models.CASCADE)
    observaciones=models.TextField(verbose_name="Observaciones")
    foto=models.ImageField(verbose_name="Foto", upload_to="clases", null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")
    
    class Meta:
        verbose_name="Aula"
        verbose_name_plural="Aulas"
        ordering=['-created']

    def __str__(self):
        return self.nombre