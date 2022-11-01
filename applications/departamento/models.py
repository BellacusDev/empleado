from django.db import models



# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    shor_name = models.CharField('Nombre Corto', max_length=20, unique=True)
    anulate = models.BooleanField('Anulado', default=False)

    class Meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural = 'Mis Departamentos'
        ordering = ['name']
        unique_together = ('name', 'shor_name')


    def __str__(self):
        return str(self.id) + ' ' + self.shor_name
