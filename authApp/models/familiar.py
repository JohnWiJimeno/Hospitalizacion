from django.db import models

class Familiar(models.Model):
    idfamiliar = models.IntegerField(primary_key=True)
    nombre = models.CharField('Nombre',max_length=20)
    apellidos = models.CharField('Apellidos',max_length=20)
    parentesto = models.CharField('Parentesco',max_length=30)
    email = models.CharField('Email',max_length=100)
    telefono = models.CharField('Telefono',max_length=15)
    
    
    

    