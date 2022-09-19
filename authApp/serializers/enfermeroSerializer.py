from rest_framework import serializers
<<<<<<< HEAD
from authApp.models.enfermero import Enfermero


class enfermeroSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Enfermero
        fields = ['idenfermero', 'nombre', 'apellido', 'correo', 'telefono','idusuario']
=======
from authApp.models.enfermero import enfermero


class enfermeroSerializer(serializers.ModelSerializer):

    class Meta:
        model: enfermero
        fields = ['idenfermero', 'nombre', 'apellidos', 'telefono', 'email', 'genero', 'user']
>>>>>>> 1c1cd8f73bb1a6ef8b6ec98743bacdee4c011e66
