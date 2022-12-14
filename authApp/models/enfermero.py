from django.db import models
from .user import User

class Enfermero(models.Model):
    idenfermero = models.IntegerField(primary_key=True)
    nombre = models.CharField('Nombre',max_length=20)
    apellidos = models.CharField('Apellidos',max_length=20)
    telefono = models.CharField('Telefono',max_length=15)
    email = models.CharField('Email',max_length=100)
    genero = models.CharField('Genero',max_length=20)
    user = models.ForeignKey(User, related_name='enfermero', on_delete=models.CASCADE)
    

    