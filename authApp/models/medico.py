from django.db import models
from .user import User



class Medico(models.Model):
    idmedico = models.IntegerField(primary_key=True)
    nombre = models.CharField('Nombre',max_length=20)
    apellidos = models.CharField('Apellido',max_length=20)
    telefono = models.CharField('Telefono',max_length=15)
    email = models.CharField('Email',max_length=100)
    especialidad = models.CharField('Especialidad',max_length=30)
    genero = models.CharField('Genero',max_length=20)
    iduser = models.ForeignKey(User, related_name='id', on_delete=models.CASCADE)
    

    