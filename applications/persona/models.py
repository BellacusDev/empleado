from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField
# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        return str(self.id) + ' ' + self.habilidad


class Empleado(models.Model):
    """ Modelo para tabla empleado"""

    JOB_CHOICES = (
        ('0', 'Contable'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro')
    )
    first_name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellido', max_length=50)
    full_name = models.CharField('Nombre completo',max_length=120, blank=True)
    job = models.CharField('Trabajo',max_length=1, choices= JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField('Fotografia', upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    class Meta:
        verbose_name = 'Mi Empleado'
        verbose_name_plural = 'Mis Empleados'
        ordering = ['last_name']
        unique_together = ('first_name', 'last_name')




    def __str__(self):
        return str(self.id) + ' ' + self.first_name + ' ' + self.last_name
