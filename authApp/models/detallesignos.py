from django.db import models

from authApp.models.signosvitales import Signosvitales
from .sugerencia import Sugerencia
from .paciente import Paciente

class Detallesignos(models.Model):
    iddetalle = models.AutoField(primary_key=True)
    idsignosvitales = models.ForeignKey(Signosvitales, related_name='idsignosvitales', on_delete=models.CASCADE) 
    idpaciente = models.ForeignKey(Paciente, related_name='idpaciente', on_delete=models.CASCADE)
    detalle = models.CharField('Detalle',max_length=500)