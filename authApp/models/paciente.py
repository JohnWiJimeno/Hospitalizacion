from datetime import date, datetime
from django.db import models
from .familiar import Familiar
from .medico import Medico
from .enfermero import Enfermero
from .auxiliar import Auxiliar
from .user import User


class Paciente(models.Model):
    idpaciente = models.IntegerField(primary_key=True)
    nombre = models.CharField('Nombre',max_length=20)
    apellidos = models.CharField('Apellido',max_length=20)
    ciudad = models.CharField('Ciudad',max_length=30)
    direccion = models.CharField('Direccion',max_length=50)
    fechanacimiento = models.DateField('Fecha', auto_now=False, auto_now_add=False)
    latitud = models.CharField('Latitud',max_length=30)
    longitud = models.CharField('Longitud',max_length=30)
    email = models.CharField('Email',max_length=100)
    idfamilar = models.ForeignKey(Familiar, related_name='paciente', on_delete=models.CASCADE)
    idmedico = models.ForeignKey(Medico, related_name='paciente', on_delete=models.CASCADE)
    idenfermero = models.ForeignKey(Enfermero, related_name='paciente', on_delete=models.CASCADE)
    idauxiliar = models.ForeignKey(Auxiliar, related_name='paciente', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='Paciente', on_delete=models.CASCADE)
    