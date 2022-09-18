from django.db import models
from .user import User

class Auxiliar(models.Model):
    idauxiliar = models.IntegerField(primary_key=True)
    nombre = models.CharField('Nombre',max_length=20)
    apellidos = models.CharField('Apellidos',max_length=20)
    telefono = models.CharField('telefono',max_length=15)
    email = models.CharField('Email',max_length=100)
    genero = models.CharField('Genero',max_length=20)
    user = models.ForeignKey(User, related_name='Auxiliar', on_delete=models.CASCADE)
    

    