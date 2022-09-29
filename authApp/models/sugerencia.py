from django.db import models

class Sugerencia(models.Model):
    idsugerencia = models.AutoField(primary_key=True)
    entorno = models.CharField('Entorno',max_length=20)
    fecha = models.DateField()
    sugerencia = models.CharField('Sugerencia',max_length=500)
    descripcion = models.CharField('Descripcion',max_length=500)
    