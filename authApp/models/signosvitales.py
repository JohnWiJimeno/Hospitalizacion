from django.db import models


class Signosvitales(models.Model):
    idsignosvitales = models.IntegerField(primary_key=True)
    nombre = models.CharField('Nombre',max_length=30)
    