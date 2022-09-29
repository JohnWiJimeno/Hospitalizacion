from django.db import models
from .paciente import Paciente
from .sugerencia import Sugerencia

class Historiaclinica(models.Model):
    idhistoria = models.AutoField(primary_key=True)
    idpaciente = models.ForeignKey(Paciente, related_name='historiaclinica', on_delete=models.CASCADE)
    idsugerencia = models.ForeignKey(Sugerencia, related_name='historiaclinica', on_delete=models.CASCADE) 
    encasa = models.BooleanField(default=1)
   
    